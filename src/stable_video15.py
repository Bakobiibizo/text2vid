import torch

from diffusers.pipelines.stable_video_diffusion.pipeline_stable_video_diffusion import (
    StableVideoDiffusionPipeline,
)
from diffusers.utils.loading_utils import load_image
from diffusers.utils.export_utils import export_to_video


def generate_video(image_path, video_path, fps):
    pipe = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid-xt",
        torch_dtype=torch.float16,
        variant="fp16",
    )
    pipe.to("cuda")

    pipe.unet = torch.compile(pipe.unet, mode="reduce-overhead")

    # Load the conditioning image
    image = load_image(image_path)
    image = image.resize((1024, 1024))

    generator = torch.manual_seed(42)
    frames = pipe(
        image,
        decode_chunk_size=8,  # type: ignore
        generator=generator,
        motion_bucket_id=180,  # type: ignore
        noise_aug_strength=0.1,  # type: ignore
    ).frames[0]
    export_to_video(frames, video_path, fps=fps)
