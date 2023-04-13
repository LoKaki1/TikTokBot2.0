import json

import requests

print(requests.post(
    "https://api.elevenlabs.io/v1/voices",
    headers={
        "xi-api-key":"97667acd3fb8308651c5204d04fb6d9c"
    }
))