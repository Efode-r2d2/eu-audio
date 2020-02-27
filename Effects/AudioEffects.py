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
import librosa
import numpy as np


def speed_change(audio_data, sr, target_speed_in_percent):
    """

    :param sr: original sampling rate
    :param audio_data: original audio time series data
    :type target_speed_in_percent: target audio speed in percent,
    positive percent means an increase in speed,
    whereas negative percent means a decrease in speed.
    """
    """Changing target audio speed in percent to rate"""
    rate = (100 - target_speed_in_percent) / 100
    """Calculating target sampling rate based on rate"""
    target_sr = sr * rate
    """Applying speed change"""
    modified_audio_data = librosa.resample(y=audio_data,
                                           orig_sr=sr,
                                           target_sr=target_sr)
    return modified_audio_data, target_sr


def time_stretch(audio_data, sr, time_stretching_in_percent):
    """

    :param sr: original sampling rate
    :param audio_data: original audio time series data
    :type time_stretching_in_percent: target audio duration in percent,
    positive percent means an increase in audio duration, whereas
    negative percent means a decrease in audio duration
    """
    """Changing time stretching in percent to rate"""
    rate = (100 + time_stretching_in_percent) / 100
    """Applying time stretching"""
    modified_audio_data = librosa.effects.time_stretch(y=audio_data, rate=rate)
    return modified_audio_data


def pitch_shift(audio_data, sr, pitch_shift_in_percent):
    """

    :param sr: original sampling rate
    :param audio_data: original time series data
    :param pitch_shift_in_percent:  pitch shift in percent,
    positive percentage means an increase in pitch, whereas
    negative percentage means a decrease in pitch.
    """

    """Here there is a conversion of required pitch modification in 
    percent to half step which is the smallest musical interval 
    commonly used in westeren tonal music. 
    One Half tone is approximately equal to 5.9463%"""

    half_steps = pitch_shift_in_percent / 5.9463
    modified_audio_data = librosa.effects.pitch_shift(y=audio_data, sr=sr, n_steps=half_steps)
    return modified_audio_data


def add_white_noise(audio_data, target_snr_in_db):
    """

    :param audio_data: original time series data
    :type target_snr_in_db: target signal to noise ratio in db
    """
    sig_power = sum(i * i for i in audio_data) / (len(audio_data))
    noise_power = sig_power / (10 ** (0.1 * target_snr_in_db))
    #sig_avg = np.mean(audio_data)
    #sig_avg_db = 10 * np.log10(np.abs(sig_avg))
    # Calculate noise db
    #noise_avg_db = sig_avg_db - target_snr_in_db
    #noise_avg = 10 ** (noise_avg_db / 10)
    # Generate white noise with a mean of zero
    mean_noise = 0.0
    noise = np.random.normal(mean_noise, np.sqrt(noise_power), len(audio_data))
    # Noise up the original signal
    modified_audio_date = audio_data + noise
    return modified_audio_date
