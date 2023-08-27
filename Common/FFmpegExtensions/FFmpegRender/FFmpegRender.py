import subprocess

from Common.FFmpegExtensions.FFmpegRender.IFFmpegRender import IFFmpegRender
from Common.FileCommon.FileCommon import save_dir, delete_file
from Common.RegularCommon.RegularCommon import device_avalible
from Configurations.VideoConnectorConfiguration.VideoConnectorConfiguration import VideoConnectorConfiguration


class FFmpegRender(IFFmpegRender):

    def __init__(self, config: VideoConnectorConfiguration):
        self.config = config
        self.device = device_avalible()
        self.device_kwargs = {'vcodec': 'h264_nvenc'} if self.device is not None else {}
        save_dir(self.config.ffmpeg_files_dir)

    def render_ffmpeg_output(self, ffmpeg_result) -> str:
        result_path = f"{self.config.result_path}{id(ffmpeg_result)}{self.config.file_format}"
        output = ffmpeg_result.output(result_path, **self.device_kwargs)
        compiled = output.compile()
        filter_complex = compiled.index('-filter_complex')
        all_of_filters = compiled[filter_complex + 1]
        script_file = f'{self.config.ffmpeg_files_dir}/{id(ffmpeg_result)}'

        with open(script_file, 'w') as file:
            file.write(all_of_filters)

        compiled_copy = compiled.copy()
        compiled_copy[filter_complex] = '-filter_complex_script'
        compiled_copy[filter_complex + 1] = script_file

        ffmpeg_video_render_result = subprocess.Popen(compiled_copy, stdin=None,
                                                      stdout=None,
                                                      stderr=None,
                                                      cwd=None).wait()

        delete_file(script_file)

        return result_path
