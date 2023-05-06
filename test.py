import whisper

model = whisper.load_model("base", device='cuda')
result = model.transcribe("./assets/background/short.mp4")
print(result['segments'])