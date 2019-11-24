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
