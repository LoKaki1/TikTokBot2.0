from typing import Union

import uvicorn
from fastapi import FastAPI

from BL.Factory.BotFactory.FFmpegAndrewTateBotCreator import FFmpegAndrewTateBotCreator
from Configurations.ConfigurationLoader import load_configuration

app = FastAPI()
# Crating Configuration
#
# app = Flask(__name__)
# cors = CORS(app, support_credentials=True)
# app.config['CORS_HEADERS'] = 'application/json'
config = load_configuration("./Configurations/config.json")
bot = FFmpegAndrewTateBotCreator(config).create_bot()
#
#
@app.post('/create/video', response_model=dict)
def create_video(request: dict):
    values = request
    voices = values['voices']
    use_voice_as_background = values.get('use_voice_as_background', False)
    background = 'minecraft'
    paths = []
    for voice in voices:
        path = bot.connect_video(voice=voice, background=background, use_voice_as_background=use_voice_as_background)
        paths.append(path)

    return {
        "paths": paths
    }

@app.get("/")
def read_root():
    return {"Hsedfdfllo": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
