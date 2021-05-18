# Task requirements
- Don't spend more than one hour on this task. One hour is enough for us to get a good idea of your coding skills, and I am sure you have better things to do 🙂
- When working on this task, feel free to use any resources, except for getting help from other people
- If you copied part of the solution from somewhere, leave the link to the source in comments
- If you write comments, please write them in English
- Use git while working on this task, like you would if this was real work. We will be looking at the commits
- Submit your solution as a git repository (Github link is preferred, but any other way is fine)
# Task description

Write a script that processes requests from a server. Instead of using a real server, requests will come from `get_random_request()` (see `dummy_server/server.py`).

The script will be run using `python3 main.py`

It should process 10 random requests before exiting:
```python
for _ in range(10):
    request = get_random_request()
    # process request
```

Each requests is an object with 3 attributes:
- `"type"` – type of request (can be `text`, `image`, `video`, or `sound`)
- `"ts"` – timestamp of when the request was sent
- `"content"` – content of the request:
  - for `text` requests – text of the message, 
  - for `image`/`video`/`sound` requests – name of the file

Each type of the request needs to be processed differently:

### `text` requests

#### If request was sent on the weekend (see `"ts"` field to determine when it was sent):
Print the emoji corresponding to what day of the week it was sent on:
- Saturday: 6️⃣
- Sunday: 7️⃣

#### Otherwise:
Print number of words in content, without counting the same word twice.
Examples:
- for message `"hi you how are you"` we print "4", because there are 4 unique words: hi, you, how, are.
- for message `"a b c b c"` we print "3"

Note: it's up to you how to deal with uppercase/lowercase, and with comma, question mark, full stop, etc, and any other edge cases you find. For example for a message like `"Hi, hi, hi"` you can either print "1" (because it only contains the word `hi`) or "3" (because it has `Hi,`, `hi,`, and `hi`)

### `image` requests

#### If file extension is JPG:
Remove file extension and print the rest of the file name.

#### Otherwise:
Print request's timestamp, but subtract 24 hours.

### `video` requests
#### If request was sent on the weekend:
Print `OK` if file extension contains 4 characters (e.g. ".webm"). Otherwise print `REJECT`

#### Otherwise:
Print `OK` if file extension contains 3 characters (e.g. ".mp4"). Otherwise print `REJECT`

### `sound` requests
Print the first unique character in content, or None if it does not exist.
For example:
- For `"qwe.mp4"`, print "q"
- For `"af.f.wav"`, print "w"
- For `"aabb"`, print None

# Extra tasks
If you have enough time left, implement:
- Ignore `image` and `video` requests if they were sent more than 4 days ago
- At the end the script (when we are done processing requests) print amount of all received requests by types
- Don't stop processing requests until we received at least 2 requests of each type.
