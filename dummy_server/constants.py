from enum import Enum


class RequestType(Enum):
    IMAGE = "image"
    TEXT = "text"
    VIDEO = "video"
    SOUND = "sound"


# These are just examples. Assume that these lists can change at any moment
DUMMY_MESSAGES = ["hi you how are you", "a b c b c", "Hey, My name is Alex, I'm 20 years old"]
DUMMY_IMAGES = ["image1.jpg", "image2.png", "image3.jpg", "image4.bmp", "image5.bmp"]
DUMMY_VIDEOS = ["video1.mkv", "video2.mp4", "video3.webm", "video4.webm", "video5.mov"]
DUMMY_SOUNDS = ["qwe.mp4", "af.f.wav", "aabb"]
