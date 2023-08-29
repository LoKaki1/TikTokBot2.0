from flask import Flask, request
from flask_cors import CORS

from BL.Factory.BotFactory.FFmpegAndrewTateBotCreator import FFmpegAndrewTateBotCreator
from Configurations.ConfigurationLoader import load_configuration

# Crating Configuration

app = Flask(__name__)
cors = CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'application/json'
config = load_configuration("./Configurations/config.json")
bot = FFmpegAndrewTateBotCreator(config).create_bot()


@app.route('/create/video', methods=['POST'])
def create_video():
    values = request.get_json()
    voices = values['voices']
    background = 'minecraft'
    paths = []
    for voice in voices:
        path = bot.connect_video(voice=voice, background=background)
        paths.append(path)

    return {
        "paths": paths
    }



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)