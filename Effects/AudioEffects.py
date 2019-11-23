import librosa
import numpy as np


def speed_change(audio_path: str, percent: float):
    """

    :param percent: required speed modification in percent,
    positive percentage means an increase in speed
    and negative percentage means a decrease in speed
    :type audio_path: path for audio location
    """
    """Changing percent """
    rate = (100 - percent) / 100
    y, sr = librosa.load(path=audio_path, offset=60.0, duration=30.0)
    y_speed = librosa.resample(y=y, orig_sr=sr, target_sr=sr * rate)
    return y_speed, sr


def time_stretch(audio_path: str, percent: float):
    """

    :param percent: required time stretching in percent
    :type audio_path: path for audio location
    """
    rate = (100 + percent) / 100
    y, sr = librosa.load(audio_path, offset=60.0, duration=30.0)
    y_stretched = librosa.effects.time_stretch(y=y, rate=rate)
    return y_stretched, sr


def pitch_shift(audio_path: str, percent: float):
    """

    :param percent: required pitch shifting in percent,
    positive percent means an increase in pitch and
    negative percent means a decrease in pitch
    :type audio_path: object
    """
    """
        Here there is a conversion of required pitch modification in 
        percent to half step which is the smallest musical interval 
        commonly used in westeren tonal music. 
        One Half tone is approximately equal to 5.9463%
    """
    half_steps = percent / 5.9463
    y, sr = librosa.load(path=audio_path, offset=60.0, duration=30.0)
    y_shifted = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=half_steps)
    return y_shifted, sr
def additive_noise(audio_path:str, percent:float):
    pass
