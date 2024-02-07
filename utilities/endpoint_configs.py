import os
from loguru import logger
from utilities.data_models import EndpointConfig, ConfigManager
from dotenv import load_dotenv

load_dotenv()


class EndpointConfigManager(ConfigManager):
    def __init__(self):
        super().__init__()
        self.environment = str(os.getenv("environment"))
        self.version = str(os.getenv("version"))
        self.hub = self.get_config("hub")
        self.text = self.get_config("text")
        self.stt = self.get_config("stt")
        self.tts = self.get_config("tts")
        self.art = self.get_config("art")
        self.fingo = self.get_config("fingo")
        self.proxy = self.get_config("proxy")
        self.mistral = self.get_config("mistral")
        self.mixtral = self.get_config("mixtral")
        self.llava = self.get_config("llava")
        self.bakllava = self.get_config("bakllava")
        self.code = self.get_config("code")
        self.video = self.get_config("video")

        self.all_config = self.set_all_config()

    def set_all_config(self):
        self.all_config = {}
        for key, value in os.environ.items():
            self.all_config[key] = value
        return self.all_config

    def get_url(self, host, port, endpoint):
        return f"http://{host}:{port}{endpoint}"

    def get_config(self, value: str):
        logger.debug(f"getting {value} config from {self.environment}")
        host = handle_error(os.getenv(f"{self.environment}_{value}_host"))
        port = handle_error(os.getenv(f"{self.environment}_{value}_port"))
        endpoint = handle_error(os.getenv(f"{self.environment}_{value}_endpoint"))

        config_map = {"host": host, "port": port, "endpoint": endpoint}

        config_map["url"] = self.get_url(**config_map)
        return EndpointConfig(**config_map)

    def set_item(self, key, value):
        value = os.getenv(f"{self.environment}_{value}")
        self.__setattr__(key, value)


def handle_error(value):
    if value is None:
        raise ValueError("value cannot be None")
    else:
        return value


def main():
    return EndpointConfigManager()


if __name__ == "__main__":
    manager = main()
    logger.debug(f"hub - {manager.hub}")
    logger.debug(f"text - {manager.text}")
    logger.debug(f"transcription - {manager.transcription}")
    logger.debug(f"art - {manager.art}")
    logger.debug(f"fingo - {manager.fingo}")
    logger.debug(f"proxy - {manager.proxy}")
    logger.debug(f"mixtral - {manager.mixtral}")
    logger.debug(f"llava - {manager.llava}")
    logger.debug(f"code - {manager.code}")
