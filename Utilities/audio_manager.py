import librosa
import soundfile as sf


def load_audio(audio_path, offset=None, duration=None):
    """

    :param duration:
    :param offset:
    :type audio_path: object
    """
    if offset is not None and duration is not None:
        audio_data, sr = librosa.load(path=audio_path, offset=offset, duration=duration)
        return audio_data, sr
    else:
        audio_data, sr = librosa.load(path=audio_path)
        return audio_data, sr


def save_audio(audio_path, audio_data, sr):
    """

    :param sr:
    :param audio_path:
    :type audio_data: object
    """
    sf.write(file=audio_path, data=audio_data, samplerate=sr)
