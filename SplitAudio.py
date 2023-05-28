from pydub import AudioSegment
audio = AudioSegment.from_wav(r"D:\test\andrewTate.wav")

for t1 in range(0, int(audio.duration_seconds), 4):
    t2 = t1 * 1000
    t3 = t2 + 4000
    newAudio = audio[t2:t3]
    newAudio.export(fr'D:\test\result\newSong{t1}.wav', format="wav")