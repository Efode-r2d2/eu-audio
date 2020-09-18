from Utilities import audio_manager
from Effects import audio_effects


def apply_speed_change(original_audio_path, modified_audio_path, target_speed_in_percent, offset=None, duration=None):
    """
    :param original_audio_path:
    :param modified_audio_path:
    :param target_speed_in_percent:
    :param offset:
    :param duration:
    """
    audio_data, sr = audio_manager.load_audio(audio_path=original_audio_path, offset=offset, duration=duration)
    modified_audio_data, target_sr = audio_effects.speed_change(audio_data=audio_data,
                                                                sr=sr,
                                                                target_speed_in_percent=target_speed_in_percent)
    audio_manager.save_audio(audio_path=modified_audio_path, audio_data=modified_audio_data, sr=sr)


def apply_time_stretching(original_audio_path, modified_audio_path, target_duration_in_percent, offset=None,
                          duration=None):
    """

    :param target_duration_in_percent:
    :param original_audio_path:
    :param modified_audio_path:
    :param offset:
    :param duration:
    """
    original_audio_data, sr = audio_manager.load_audio(audio_path=original_audio_path, offset=offset, duration=duration)
    modified_audio_data = audio_effects.time_stretch(audio_data=original_audio_data,
                                                     sr=sr,
                                                     time_stretching_in_percent=target_duration_in_percent)
    audio_manager.save_audio(audio_path=modified_audio_path, audio_data=modified_audio_data, sr=sr)


def apply_pitch_shifting(original_audio_path, modified_audio_path, target_pitch_shift_in_percent, offset=None,
                         duration=None):
    """

    :param target_pitch_shift_in_percent:
    :param original_audio_path:
    :param modified_audio_path:
    :param offset:
    :param duration:
    """
    original_audio_data, sr = audio_manager.load_audio(audio_path=original_audio_path,
                                                       offset=offset,
                                                       duration=duration)
    modified_audio_data = audio_effects.pitch_shift(audio_data=original_audio_data,
                                                    sr=sr,
                                                    pitch_shift_in_percent=target_pitch_shift_in_percent)
    audio_manager.save_audio(audio_path=modified_audio_path, audio_data=modified_audio_data, sr=sr)


def add_white_noise(original_audio_path, modified_audio_path, target_snr_in_db, offset=None, duration=None):
    """

    :param original_audio_path:
    :param modified_audio_path:
    :param target_snr_in_db:
    :param offset:
    :param duration:
    """
    original_audio_data, sr = audio_manager.load_audio(audio_path=original_audio_path, offset=offset, duration=duration)
    modified_audio_data = audio_effects.add_white_noise(audio_data=original_audio_data,
                                                        target_snr_in_db=target_snr_in_db)
    audio_manager.save_audio(audio_path=modified_audio_path, audio_data=modified_audio_data, sr=sr)
