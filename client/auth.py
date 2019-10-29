from dynaconf import settings
from .utils.encoders import ObjectJsonSerializable


class Auth(ObjectJsonSerializable):
    def __init__(self, galaxId=None, galaxHash=None):
        self.galaxId = galaxId
        self.galaxHash = galaxHash

    def read_config(self):
        self.galaxId = settings.get('galaxId')
        self.galaxHash = settings.get('galaxHash')
