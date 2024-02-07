import base64
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from utilities.endpoint_configs import EndpointConfigManager
from utilities.data_models import VideoGenerationRequest, VideoGenerationResponse
from src.image import generate_image
from src.stable_video_xt import generate_video
from src.transient import transient_tracker
from main import main as generate_video_main
import loguru

logger = loguru.logger

manager = EndpointConfigManager()
config = manager.video

logger.debug(config)
# from fastapi import WebSocket

# async def cache_control(request:web.Request, handler)

# class WebSocketManager:
#    def __init__(self):
#        self.active_connections: Dict[str, WebSocket] = {}
#
#    async def connect(self, websocket: WebSocket, client_id: str):
#        await websocket.accept()
#        self.active_connections[client_id] = websocket
#
#
#    async def disconnect(self, client_id: str):
#        del self.active_connections[client_id]
#        # Handle client disconnection logic
#
#    async def send_message(self, client_id: str, message: str):
#        websocket = self.active_connections.get(client_id)
#        if websocket:
#            await websocket.send_text(message)
#        else:
#            # Handle case where client is no longer connected
#
#    async def broadcast_message(self, message: str):
#        for websocket in self.active_connections.values():
#            await websocket.send_text(message)
#        # Handle broadcasting message to all connected clients
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/data", StaticFiles(directory="data"), name="data")


@app.get("/")
def root():
    return "<h1>/docs for more information</h1>"


@logger.catch()
@app.post(config.endpoint)
def video_generation(request: VideoGenerationRequest):
    logger.info("Generating Video")
    logger.debug(request)
    try:
        filename = generate_video_main(
            request.prompt,
        )
        video_path = f"data/{filename}.mp4"
        with open(video_path, "rb") as f:
            base64_video = base64.b64encode(f.read()).decode("utf-8")
        HTTPResponse = {
            "filename": filename,
            "video": base64_video,
        }
        logger.debug(HTTPResponse)
        return HTTPResponse

    except Exception as e:
        logger.exception(e)
        return {"error": str(e)}


@logger.catch()
def to_base64(file):
    return base64.b64encode(open(file, "rb").read()).decode("utf-8")


if __name__ == "__main__":
    uvicorn.run("api:app", host=config.host, port=int(config.port), reload=True)

# @app.websocket("/ws")
# async def video_generation(request: VideoGenerationRequest):
#    await websocket.accept()
#
#    while True:
#        data = await websocket.receive_json()
#        request = VideoGenerationRequest(**request.model_dump())
#        generate_video(
#            request.prompt,
#            request.temp_image_path,
#            request.temp_video_path,
#            request.temp_audio_path,
#        )
