"""

    Class Name: AudioEffects
    Author: Efriem Desalew, efidesalew@gmail.com
    Date: November,2019

"""
import librosa
import numpy as np


class AudioEffects(object):
    def __init__(self, audio_data, sr):
        """

        :type sr: original audio sampling rate
        :type audio_data: original time series audio data
        """
        self.audio_data = audio_data
        self.sr = sr

    def speed_change(self, target_speed_in_percent):
        """

        :type target_speed_in_percent: target audio speed in percent,
        positive percent means an increase in speed,
        whereas negative percent means a decrease in speed.
        """
        """Changing target audio speed in percent to rate"""
        rate = (100 - target_speed_in_percent) / 100
        """Calculating target sampling rate based on rate"""
        target_sr = self.sr * rate
        """Applying speed change"""
        modified_audio_data = librosa.resample(y=self.audio_data,
                                               orig_sr=self.sr,
                                               target_sr=target_sr)
        return modified_audio_data, target_sr

    def time_stretch(self, time_stretching_in_percent):
        """

        :type time_stretching_in_percent: target audio duration in percent,
        positive percent means an increase in audio duration, whereas
        negative percent means a decrease in audio duration
        """
        """Changing time stretching in percent to rate"""
        rate = (100 + time_stretching_in_percent) / 100
        """Applying time stretching"""
        modified_audio_data = librosa.effects.time_stretch(y=self.audio_data, rate=rate)
        return modified_audio_data, self.sr

    def pitch_shift(self, pitch_shift_in_percent):
        """

        :param pitch_shift_in_percent:  pitch shift in percent,
        positive percentage means an increase in pitch, whereas
        negative percentage means a decrease in pitch.
        """

        """Here there is a conversion of required pitch modification in 
        percent to half step which is the smallest musical interval 
        commonly used in westeren tonal music. 
        One Half tone is approximately equal to 5.9463%"""

        half_steps = pitch_shift_in_percent / 5.9463
        modified_audio_data = librosa.effects.pitch_shift(y=self.audio_data, sr=self.sr, n_steps=half_steps)
        return modified_audio_data, self.sr

    def add_white_noise(self, target_snr_in_db):
        """

        :type target_snr_in_db: target signal to noise ratio in db
        """
        sig_avg = np.mean(self.audio_data)
        sig_avg_db = 10 * np.log10(np.abs(sig_avg))
        # Calculate noise db
        noise_avg_db = sig_avg_db - target_snr_in_db
        noise_avg = 10 ** (noise_avg_db / 10)
        # Generate white noise with a mean of zero
        mean_noise = 0.0
        noise = np.random.normal(mean_noise, np.sqrt(noise_avg), len(self.audio_data))
        # Noise up the original signal
        modified_audio_date = self.audio_data + noise
        return modified_audio_date, self.sr
