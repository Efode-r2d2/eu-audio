"""
    <ed-Audio is an open source audio processing toolbox>
    Copyright (C) <2019>  <Efriem Desalew Gebie>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from Utilities import AudioManager
from Effects import AudioEffects


def apply_speed_change(original_audio_path, modified_audio_path, target_speed_in_percent, offset=None, duration=None):
    """
    :param original_audio_path:
    :param modified_audio_path:
    :param target_speed_in_percent:
    :param offset:
    :param duration:
    """
    audio_data, sr = AudioManager.load_audio(audio_path=original_audio_path, offset=offset, duration=duration)
    modified_audio_data, target_sr = AudioEffects.speed_change(audio_data=audio_data,
                                                               sr=sr,
                                                               target_speed_in_percent=target_speed_in_percent)
    AudioManager.save_audio(audio_path=modified_audio_path, audio_data=modified_audio_data, sr=target_sr)


def apply_time_stretching(original_audio_path, modified_audio_path, target_duration_in_percent, offset=None,
                          duration=None):
    """

    :param target_duration_in_percent:
    :param original_audio_path:
    :param modified_audio_path:
    :param offset:
    :param duration:
    """
    original_audio_data, sr = AudioManager.load_audio(audio_path=original_audio_path, offset=offset, duration=duration)
    modified_audio_data = AudioEffects.time_stretch(audio_data=original_audio_data,
                                                    sr=sr,
                                                    time_stretching_in_percent=target_duration_in_percent)
    AudioManager.save_audio(audio_path=modified_audio_path, audio_data=modified_audio_data, sr=sr)


def apply_pitch_shifting(original_audio_path, modified_audio_path, target_pitch_shift_in_percent, offset=None,
                         duration=None):
    """

    :param target_pitch_shift_in_percent:
    :param original_audio_path:
    :param modified_audio_path:
    :param offset:
    :param duration:
    """
    original_audio_data, sr = AudioManager.load_audio(audio_path=original_audio_path,
                                                      offset=offset,
                                                      duration=duration)
    modified_audio_data = AudioEffects.pitch_shift(audio_data=original_audio_data,
                                                   sr=sr,
                                                   pitch_shift_in_percent=target_pitch_shift_in_percent)
    AudioManager.save_audio(audio_path=modified_audio_path, audio_data=modified_audio_data, sr=sr)


def add_white_noise(original_audio_path, modified_audio_path, target_snr_in_db, offset=None, duration=None):
    """

    :param original_audio_path:
    :param modified_audio_path:
    :param target_snr_in_db:
    :param offset:
    :param duration:
    """
    original_audio_data, sr = AudioManager.load_audio(audio_path=original_audio_path, offset=offset, duration=duration)
    modified_audio_data = AudioEffects.add_white_noise(audio_data=original_audio_data,
                                                       target_snr_in_db=target_snr_in_db)
    AudioManager.save_audio(audio_path=modified_audio_path, audio_data=modified_audio_data, sr=sr)
