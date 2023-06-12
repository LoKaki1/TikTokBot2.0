import ffmpeg
from moviepy.audio.AudioClip import concatenate_audioclips

from BL.Factory.MetadataFactory.ImageTextFactory import ImageTextFactory
from BL.VideoConnector.IVideoConnector import IVideoConnector
from BL.VideoParts.BackgroundCreator.IBackgroundCreator import IBackgroundCreator
from BL.VideoParts.FrontCreator.FFMpegFrontCreator.FFmpegImageCreator.OverlayImages import OverlayImages
from BL.VideoParts.VoiceCreator.IVoiceCreator import IVoiceCreator
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration
from Configurations.VoiceConfiguration.VoiceConfiguration import VoiceConfiguration
from Pullers.VoicePuller.IVoicePuller import IVoicePuller


class FFmpegRedditVideoConnector(IVideoConnector):

    def __init__(self,
                 background_creator: IBackgroundCreator,
                 video_connector_config: VideoConnectorConfiguration,
                 voice_creator: IVoiceCreator,
                 overlay_images: OverlayImages,
                 image_text_factory: ImageTextFactory,
                 voice_puller: IVoicePuller,
                 voice_configuration: VoiceConfiguration
                 ):
        self.voice_configuration = voice_configuration
        self.voice_puller = voice_puller
        self.image_text_factory = image_text_factory
        self.voice_creator = voice_creator
        self.overlay_images = overlay_images
        self.config = video_connector_config
        self.background_creator = background_creator

    def connect_video(self, *args, **kwargs):
        background_name = kwargs['background']
        submission = kwargs['submission']
        [_, texts] = self.image_text_factory.create_images_text(submission)
        voices = self.voice_creator.create_voice(texts, background_name)
        audio_concat = concatenate_audioclips(voices[1])
        audio_concat.write_audiofile((path := f"{self.voice_configuration.output_dir}{id(voices)}.wav"))
        ffmpeg_base = self.background_creator.create_background(background_name, voices[0].duration).background_data
        result_path = f"{self.config.result_path}{id(voices)}{self.config.file_format}"
        ffmpeg_base_images = self.overlay_images.connect_image_voice(submission, ffmpeg_base)
        ffmpeg_base_images = ffmpeg.concat(ffmpeg_base_images[0], ffmpeg.input(path), v=1, a=1)

        return ffmpeg_base_images.output(result_path,).run()