from datetime import datetime

from enum import Enum

from pydantic import BaseModel

class ServerDataType(str, Enum):
    sound = 'sound'
    image = 'image'
    video = 'video'
    text = 'text'


class ServerData(BaseModel):
    type: ServerDataType
    ts: datetime
    content: str