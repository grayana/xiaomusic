from pydantic import BaseModel


class PauseRequest(BaseModel):
    deviceId: str

class PlayRequest(BaseModel):
    deviceId: str

class actionRequest(BaseModel):
    deviceId: str
    action: str