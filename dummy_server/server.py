import random
from dummy_server.constants import RequestType, DUMMY_MESSAGES, DUMMY_IMAGES, DUMMY_VIDEOS, DUMMY_SOUNDS
from datetime import datetime
from time import time


def get_random_request():
    """
    Return random request
    :rtype: dict
    """
    # generate data for request
    req_type = random.choice(list(RequestType)).value

    return {
        "type": req_type,
        "ts": _get_random_date(),
        "content": _get_random_content(req_type),
    }


def _get_random_date():
    """
    Generate random date roughly between now and 10 days ago
    :rtype: datetime.datetime
    """
    rand_ts = random.randint(0, 999999)
    return datetime.fromtimestamp(time() - rand_ts)


def _get_random_content(req_type):
    """
    Generate random content for request

    :param req_type: request type
    :type req_type: RequestType

    :rtype: str
    """
    if req_type == RequestType.TEXT.value:
        return random.choice(DUMMY_MESSAGES)
    elif req_type == RequestType.IMAGE.value:
        return random.choice(DUMMY_IMAGES)
    elif req_type == RequestType.VIDEO.value:
        return random.choice(DUMMY_VIDEOS)
    elif req_type == RequestType.SOUND.value:
        return random.choice(DUMMY_SOUNDS)
    else:
        raise Exception("Received unsupported request type")
