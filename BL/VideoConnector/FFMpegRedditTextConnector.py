import ffmpeg
from moviepy.audio.AudioClip import concatenate_audioclips

from BL.Factory.MetadataFactory.ImageTextFactory import ImageTextFactory
from BL.VideoConnector.IVideoConnector import IVideoConnector
from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator
from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawText.IDrawText import IDrawText
from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFMpegTextCreator.DrawTextCreator import DrawTextCreator
from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFmpegImageCreator.OverlayImages import OverlayImages
from BL.VideoParts.VoiceCreator.IVoiceCreator import IVoiceCreator
from Common.Factory.STTModelFactory.ISTTModelFactory import ISTTModelFactory
from Common.Models.STTModel import STTModel
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration
from Configurations.VoiceConfiguration.VoiceConfiguration import VoiceConfiguration
from Pullers.FrontContentPuller.TextPuller.STTPuller.ISTTPuller import ISTTPuller
from Pullers.VoicePuller.IVoicePuller import IVoicePuller


class FFMpegRedditTextConnector(IVideoConnector):

    def __init__(self,
                 background_creator: IBackgroundCreator,
                 video_connector_config: VideoConnectorConfiguration,
                 voice_creator: IVoiceCreator,
                 overlay_images: OverlayImages,
                 image_text_factory: ImageTextFactory,
                 voice_puller: IVoicePuller,
                 voice_configuration: VoiceConfiguration,
                 draw_text: IDrawText,
                 stt_model_factory: ISTTModelFactory,
                 stt_puller: ISTTPuller):
        self.stt_puller = stt_puller
        self.stt_model_factory = stt_model_factory
        self.voice_configuration = voice_configuration
        self.voice_puller = voice_puller
        self.image_text_factory = image_text_factory
        self.voice_creator = voice_creator
        self.overlay_images = overlay_images
        self.config = video_connector_config
        self.background_creator = background_creator
        self.draw_text = draw_text

    def connect_video(self, *args, **kwargs):
        background_name = kwargs['background']
        submission = kwargs['submission']
        [_, texts] = self.image_text_factory.create_images_text(submission, 2)
        voices = self.voice_creator.create_voice(texts, background_name)
        comments_text_models: list[STTModel] = []
        start_time = self.stt_puller.pull_text_from_audio(voices[1][0].filename)[-1].end_time

        for index, voice in enumerate(voices[1]):
            if not index:

                continue

            comment_stt_model = self.stt_puller.pull_text_from_audio(voice.filename)
            print(index - 1, len(comments_text_models))

            for model in comment_stt_model:
                model.start_time = start_time
                model.end_time += model.start_time
                model.duration = model.end_time - model.start_time
                start_time = model.end_time

            comments_text_models += comment_stt_model

        audio_concat = concatenate_audioclips(voices[1])

        audio_concat.write_audiofile((path := f"{self.voice_configuration.output_dir}{id(voices)}.wav"))
        ffmpeg_base = self.background_creator.create_background(background_name, voices[0].duration).background_data
        result_path = f"{self.config.result_path}{id(voices)}{self.config.file_format}"
        ffmpeg_base_images = self.overlay_images.connect_image_voice(submission, 0, ffmpeg_base)[0]
        ffmpeg_base_images = self.draw_text.draw_text(comments_text_models, ffmpeg_base_images)
        ffmpeg_base_images = ffmpeg.concat(ffmpeg_base_images, ffmpeg.input(path), v=1, a=1)

        return ffmpeg_base_images.output(result_path,).run()