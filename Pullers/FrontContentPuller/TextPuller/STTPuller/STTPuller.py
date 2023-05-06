from typing import List
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

from Common.FileCommon import FileCommon
from Common.LoggerCommon.Logger import log_info
from Common.Models.STTModel import STTModel
from Pullers.FrontContentPuller.TextPuller.STTPuller.ISTTPuller import ISTTPuller


class STTPuller(ISTTPuller):

    def pull_text_from_audio(self, path: str) -> List[STTModel]:
        """
        :param path:
        :return:
        """
        file_format = path.split('.')[-1]
        audio = AudioSegment.from_file(path, format=file_format)
        folder = f'./assets/sound/{id(audio)}'
        FileCommon.save_dir(folder)
        '''
        Step #1 - Slicing the audio file into smaller chunks.
        '''
        # Length of the audiofile in milliseconds
        n = len(audio)

        # Variable to count the number of sliced chunks
        counter = 1

        # Text file to write the recognized audio

        # Interval length at which to slice the audio file.
        # If length is 22 seconds, and interval is 5 seconds,
        # The chunks created will be:
        # chunk1 : 0 - 5 seconds
        # chunk2 : 5 - 10 seconds
        # chunk3 : 10 - 15 seconds
        # chunk4 : 15 - 20 seconds
        # chunk5 : 20 - 22 seconds
        interval = 5 * 1000

        # Length of audio to overlap.
        # If length is 22 seconds, and interval is 5 seconds,
        # With overlap as 1.5 seconds,
        # The chunks created will be:
        # chunk1 : 0 - 5 seconds
        # chunk2 : 3.5 - 8.5 seconds
        # chunk3 : 7 - 12 seconds
        # chunk4 : 10.5 - 15.5 seconds
        # chunk5 : 14 - 19.5 seconds
        # chunk6 : 18 - 22 seconds
        overlap = 1.5 * 1000
        text = ''
        # Initialize start and end seconds to 0
        start = 0
        end = 0

        # Flag to keep track of end of file.
        # When audio reaches its end, flag is set to 1 and we break
        flag = 0
        text_t = []
        # Iterate from 0 to end of the file,
        # with increment = interval

        r = sr.Recognizer()
        # Store the sliced audio file to the defined path
        for counter, i in enumerate(audio):

            filename = f'{folder}/chunk{str(counter)}.wav'

            i.export(filename, format="wav")

            with sr.AudioFile(filename) as source:
                audio_listened = r.listen(source)

                rec = r.recognize_google(audio_listened)
                model = STTModel(rec, (n - 0) / 1000, 0 / n, end / 1000, filename)
                text_t.append(model)

        # for i in range(0, 2 * n, interval):
        #
        #     # During first iteration,
        #     # start is 0, end is the interval
        #     if i == 0:
        #         start = 0
        #         end = interval
        #
        #     # All other iterations,
        #     # start is the previous end - overlap
        #     # end becomes end + interval
        #     else:
        #         start = end - overlap
        #         end = start + interval
        #
        #     # When end becomes greater than the file length,
        #     # end is set to the file length
        #     # flag is set to 1 to indicate break.
        #     if end >= n:
        #         end = n
        #         flag = 1
        #
        #     # Storing audio file from the defined start to end
        #     chunk = audio[start:end]
        #
        #     # Filename / Path to store the sliced audio
        #
        #
        #     # Print information about the current chunk
        #     print("Processing chunk " + str(counter) + ". Start = "
        #           + str(start) + " end = " + str(end))
        #
        #     # Increment counter for the next chunk
        #     counter = counter + 1
        #
        #     # Slicing of the audio file is done.
        #     # Skip the below steps if there is some other usage
        #     # for the sliced audio files.
        #
        #     '''
        #     Step #2 - Recognizing the chunk and writing to a file.
        #     '''
        #
        #     # Here, Google Speech Recognition is used
        #     # to take each chunk and recognize the text in it.
        #
        #     # Specify the audio file to recognize
        #
        #     AUDIO_FILE = filename
        #
        #     # Initialize the recognizer
        #     r = sr.Recognizer()
        #
        #     # Traverse the audio file and listen to the audio
        #     with sr.AudioFile(AUDIO_FILE) as source:
        #         audio_listened = r.listen(source)
        #
        #     # Try to recognize the listened audio
        #     # And catch exceptions.
        #     try:
        #         rec = r.recognize_google(audio_listened)
        #
        #         # If recognized, write into the file.
        #         text += rec + " "
        #         model = STTModel(rec, (end - start) / 1000, start / 1000, end / 1000, filename)
        #         text_t.append(model)
        #
        #     # If google could not understand the audio
        #     except sr.UnknownValueError:
        #         print("Could not understand audio")
        #
        #     # If the results cannot be requested from Google.
        #     # Probably an internet connection error.
        #     except sr.RequestError as e:
        #         print("Could not request results.")
        #
        #     # Check for flag.
        #     # If flag is 1, end of the whole audio reached.
        #     # Close the file and break.
        #     if flag == 1:
        #         break
        log_info(text_t)
        return text_t
        # importing libraries
#
#
# # create a speech recognition object
# r = sr.Recognizer()
#
# # a function that splits the audio file into chunks
# # and applies speech recognition
# def get_large_audio_transcription(path):
#     """
#     Splitting the large audio file into chunks
#     and apply speech recognition on each of these chunks
#     """
#     # open the audio file using pydub
#
#     # split audio sound where silence is 700 miliseconds or more and get chunks
#
#     folder_name = "audio-chunks"
#     # create a directory to store the audio chunks
#     if not os.path.isdir(folder_name):
#         os.mkdir(folder_name)
#     whole_text = ""
#     # process each chunk
#     for i, audio_chunk in enumerate(chunks, start=1):
#         # export audio chunk and save it in
#         # the `folder_name` directory.
#         chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
#         audio_chunk.export(chunk_filename, format="wav")
#         # recognize the chunk
#         with sr.AudioFile(chunk_filename) as source:
#             audio_listened = r.record(source)
#             # try converting it to text
#             try:
#                 text = r.recognize_google(audio_listened)
#             except sr.UnknownValueError as e:
#                 print("Error:", str(e))
#             else:
#                 text = f"{text.capitalize()}. "
#                 print(chunk_filename, ":", text)
#                 whole_text += text
#     # return the text for all chunks detected
#     return whole_text

