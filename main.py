import datetime
from datetime import timedelta

from dummy_server.server import get_random_request

# Dummy server generates random requests, 
# your goal is to process them as per task requirements (see README.md)

def text_response(request):
    if request["ts"].isoweekday() == 6:
        return "\U00000036"
    elif request["ts"].isoweekday() == 7:
         return "\U00000037"
    else:
        words = list(set(request["content"].split()))
        return len(words)

def image_response(request):
    if request["content"][-3:] == "jpg":
         return request["content"][0:-4]
    else:
        return request["ts"] - timedelta(days = 1)

def video_response(request):
    response  = "REJECT"
    if request["ts"].isoweekday() in [6, 7]:
        if request["content"][-4] == ".":
            response = "ok"
    else:
        if request["content"][-3] == ".":
            response = "ok"
    return response

def sound_response(request):
    content = request["content"]
    unique_letter = None
    for letter in content:
        if content.count(letter) == 1:
            unique_letter = letter
            break
    return unique_letter


if __name__ == "__main__":
    requests_statistic = {
            "text":0,
            "image":0,
            "video":0,
            "sound":0,
        }
    processing = True
    while processing:
        request = get_random_request()
        print(request)
        # process request below
        type_objects = request["type"]
        relevant_request = datetime.datetime.now() - timedelta(days = 4)
        if type_objects == "text":
            print(text_response(request))
        elif type_objects == "image":
            print(image_response(request))
        elif type_objects == "video" and request["ts"] >= relevant_request:
            print(video_response(request))
        elif type_objects == "sound":
            print(sound_response(request))
        requests_statistic[type_objects] += 1
        # check of 2 requests
        processing = False
        for kye, value in requests_statistic.items():
            if value < 2:
                processing = True
    print("__________________")
    print("\nRequest statistic:\n")
    for key, value in requests_statistic.items():
        print(key, value)
