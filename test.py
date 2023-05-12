import ffmpeg

in_file = ffmpeg.input('./assets/videos/minecraft.mp4')
overlay_file = ffmpeg.input('overlay.png')

text = [['hi there', (0, 631)], ['my name is shahar', (631, 1000)]]

filters = []
for (text, (start_time, end)) in text:
    filters.append(ffmpeg.drawtext(in_file, text, 0, 0))
data = ffmpeg.drawtext(in_file, "dasdasd")
run_data = data.output('out15.mp4', **{'c:v': 'h264_nvenc'})
run_data.run()