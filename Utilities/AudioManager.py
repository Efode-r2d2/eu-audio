"""
    Class Name: AudioManager
    Author: Efriem Desalew, efidesalew@gmial.com
    Date: November, 2019
"""
import librosa


class AudioManager(object):
    def __init(self, audio_path):
        self.audio_path = audio_path

    def load_audio(self, offset=None, duration=None):
        if offset is not None and duration is not None:
            audio_data, sr = librosa.load(path=self.audio_path, offset=offset, duration=duration)
            return audio_data, sr
        else:
            audio_data, sr = librosa.load(path=self.audio_path)
