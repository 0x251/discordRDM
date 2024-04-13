import json

from ..errors.errors import Logging

class JsonParser:
    def __init__(self) -> None:
        Logging.log_info("Parsed DisRDM config")
        with open("config.json") as file:
            self.config_data = json.load(file)
    
    def get_config_value(self, key: str):
        return self.config_data["Disrdm"].get(key, None)
    
    def threads(self):
        return self.get_config_value("threads")

    def proxies(self):
        return self.get_config_value("proxies")

    def auth_token(self):
        return self.get_config_value("Auth-Token")

    def session_token(self):
        return self.get_config_value("Session-Token")

    def logging(self):
        return self.get_config_value("Logging")
