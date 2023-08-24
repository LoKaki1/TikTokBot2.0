from Common.Models.STTModel import STTModel


def calc_parabola_vertex(x1, y1, x2, y2, x3, y3):
    '''
		Adapted and modifed to get the unknowns for defining a parabola:
		http://stackoverflow.com/questions/717762/how-to-calculate-the-vertex-of-a-parabola-given-three-points
		'''
    denom = (x1 - x2) * (x1 - x3) * (x2 - x3)
    A = (x3 * (y2 - y1) + x2 * (y1 - y3) + x1 * (y3 - y2)) / denom
    B = (x3 * x3 * (y1 - y2) + x2 * x2 * (y3 - y1) + x1 * x1 * (y2 - y3)) / denom
    C = (x2 * x3 * (x2 - x3) * y1 + x3 * x1 * (x3 - x1) * y2 + x1 * x2 * (x1 - x2) * y3) / denom

    return A, B, C


models = [STTModel(text=' What', duration=0.40000000000000036, start_time=4.22, end_time=4.62),
          STTModel(text=' footwear', duration=0.17999999999999972, start_time=4.62, end_time=4.8),
          STTModel(text=' do', duration=0.21999999999999975, start_time=4.8, end_time=5.02),
          STTModel(text=' I', duration=0.10000000000000053, start_time=5.02, end_time=5.12),
          STTModel(text=' use', duration=0.21999999999999975, start_time=5.12, end_time=5.34),
          STTModel(text=' in', duration=0.20000000000000018, start_time=5.34, end_time=5.54),
          STTModel(text=' the', duration=0.1200000000000001, start_time=5.54, end_time=5.66),
          STTModel(text=' gym?', duration=0.21999999999999975, start_time=5.66, end_time=5.88),
          STTModel(text=' What', duration=0.040000000000000036, start_time=6.14, end_time=6.18),
          STTModel(text=' do', duration=0.10000000000000053, start_time=6.18, end_time=6.28),
          STTModel(text=' I', duration=0.1200000000000001, start_time=6.28, end_time=6.4),
          STTModel(text=' wear', duration=0.1999999999999993, start_time=6.4, end_time=6.6),
          STTModel(text=' to', duration=0.3200000000000003, start_time=6.6, end_time=6.92),
          STTModel(text=' squat', duration=0.5999999999999996, start_time=6.92, end_time=7.52),
          STTModel(text=' to', duration=0.3000000000000007, start_time=7.52, end_time=7.82),
          STTModel(text=' bench?', duration=0.6600000000000001, start_time=7.82, end_time=8.48),
          STTModel(text=' Most', duration=0.14000000000000057, start_time=8.68, end_time=8.82),
          STTModel(text=' of', duration=0.16000000000000014, start_time=8.82, end_time=8.98),
          STTModel(text=' the', duration=0.05999999999999872, start_time=8.98, end_time=9.04),
          STTModel(text=' time', duration=0.08000000000000007, start_time=9.04, end_time=9.12),
          STTModel(text=' I', duration=0.120000000000001, start_time=9.12, end_time=9.24),
          STTModel(text=' have', duration=0.11999999999999922, start_time=9.24, end_time=9.36),
          STTModel(text=' no', duration=0.20000000000000107, start_time=9.36, end_time=9.56),
          STTModel(text=' idea', duration=0.27999999999999936, start_time=9.56, end_time=9.84),
          STTModel(text=' what', duration=0.1999999999999993, start_time=9.84, end_time=10.04),
          STTModel(text=' shoes', duration=0.3000000000000007, start_time=10.04, end_time=10.34),
          STTModel(text=' to', duration=0.17999999999999972, start_time=10.34, end_time=10.52),
          STTModel(text=' use', duration=0.14000000000000057, start_time=10.52, end_time=10.66),
          STTModel(text=' to', duration=0.17999999999999972, start_time=10.66, end_time=10.84),
          STTModel(text=' squat', duration=0.2599999999999998, start_time=10.84, end_time=11.1),
          STTModel(text=' the', duration=0.17999999999999972, start_time=11.1, end_time=11.28),
          STTModel(text=' bench.', duration=0.1800000000000015, start_time=11.28, end_time=11.46),
          STTModel(text=' Using', duration=0.20000000000000107, start_time=11.62, end_time=11.82),
          STTModel(text=' typical', duration=0.4599999999999991, start_time=11.82, end_time=12.28),
          STTModel(text=' running', duration=0.3200000000000003, start_time=12.28, end_time=12.6),
          STTModel(text=' shoes', duration=0.28000000000000114, start_time=12.6, end_time=12.88),
          STTModel(text=' or', duration=0.1399999999999988, start_time=12.88, end_time=13.02),
          STTModel(text=' tennis', duration=0.2400000000000002, start_time=13.02, end_time=13.26),
          STTModel(text=' shoes', duration=0.2400000000000002, start_time=13.26, end_time=13.5),
          STTModel(text=' is', duration=0.1999999999999993, start_time=13.5, end_time=13.7),
          STTModel(text=' the', duration=0.16000000000000014, start_time=13.7, end_time=13.86),
          STTModel(text=' worst', duration=0.28000000000000114, start_time=13.86, end_time=14.14),
          STTModel(text=' idea.', duration=0.41999999999999993, start_time=14.14, end_time=14.56),
          STTModel(text=' Did', duration=0.08000000000000007, start_time=14.72, end_time=14.8),
          STTModel(text=' you?', duration=0.17999999999999972, start_time=14.8, end_time=14.98)]

base_size = 30
max_size = 60
for text_model in models:
    t = text_model.start_time
    duration_multiplication = 12.6 // text_model.duration

    while t - text_model.start_time < text_model.end_time - text_model.start_time:
        # if t-text_model.start_time < (text_model.end_time - t) / 2:
        #     print(50 * (1 + 2 * (t - text_model.start_time)))
        # else:
        #     print((50 * (1 + 2 * (t - text_model.start_time)) / (1 + (t - (text_model.end_time - text_model.start_time * 2) / 3))))
        # math_term = (text_model.end_time + text_model.start_time * 2) / 3
        # what = 50 * (1 + 2 * (math_term - text_model.start_time))
        # data = round(50 * 2 * (1 + 2 * (t - text_model.start_time)))\
        #     if t - text_model.start_time < (text_model.end_time - t) / 2\
        #     else round(50 / (1 + 2 * (t - math_term)) + (what - 50))
        # p = 12.6 / (text_model.duration) * (t - text_model.start_time)
        # data = - p ** 3 + 12*p**2 +10 * p + 30
        #     data = round(-(duration_multiplication * (t - text_model.start_time)) * (duration_multiplication * (t - text_model.start_time)) * (duration_multiplication * (t - text_model.start_time)) + 12 * (duration_multiplication * (t - text_model.start_time)) * (duration_multiplication * (t - text_model.start_time)) + 10 * (duration_multiplication * (t - text_model.start_time)) + 30)
        x = (t - text_model.start_time)

        x1, y1 = (0, base_size)
        x2, y2 = (text_model.duration / 2, max_size)
        x3, y3 = (text_model.duration, base_size)
        a, b, c = calc_parabola_vertex(x1, y1, x2, y2, x3, y3)
        data = a * x ** 2 + b * x + c
        print(data)
        t += 0.01

