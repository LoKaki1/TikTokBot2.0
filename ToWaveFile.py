import subprocess

input_file = "./assets/background/short.mp4"
output_file = "short.wav"

command = ["ffmpeg", "-i", input_file, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", output_file]
subprocess.call(command)