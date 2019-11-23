import librosa
import numpy as np


def speed_change(audio_path: str, percent: float):
    """

    :param percent: required speed modification in percent,
    positive percentage means an increase in percent
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


def pitch_shifting(audio_path: str, percent: float):
    """

    :param percent: 
    :type audio_path: object
    """
    steps = percent / 5.9463
    y, sr = librosa.load(path=audio_path, offset=60.0, duration=30.0)
    y_shifted = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=steps)
    return y_shifted, sr
