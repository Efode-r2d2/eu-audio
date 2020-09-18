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
from Utilities import directory_manager
from EffectsManager import effects_manager

# source directory
src_dir = "../../Test_Data/Reference_Audios"
# destination directory for modified audios
dist_dir = "../../Test_Data/Modified_Audios/White_Noise"
# searching for all .mp3 files in a given source directory
mp3_files = directory_manager.find_mp3_files(source_dir=src_dir)
# adding white noise to the fourth audio
original_audio_path = mp3_files[0]
file_name = original_audio_path.split("/")[4].split(".")[0]
print("Original Audio Path: ", original_audio_path)
print("File Name: ", file_name)
# adding white noise with target signal to noise ratio of
# -10 dB to a portion of audio specified by offset and
# duration parameters
effects_manager.add_white_noise(original_audio_path=original_audio_path,
                                modified_audio_path=dist_dir+"/"+file_name+str(-10)+".wav",
                                target_snr_in_db=-10,
                                offset=10.0,
                                duration=20.0)
print("Modified Audio Saved Here: ", dist_dir+"/"+file_name+str(-10)+".wav")
# adding white noise with target signal to noise ratio of
# 10 dB to a portion of audio specified by offset and
# duration parameters
effects_manager.add_white_noise(original_audio_path=original_audio_path,
                                modified_audio_path=dist_dir+"/"+file_name+str(10)+".wav",
                                target_snr_in_db=10,
                                offset=10.0,
                                duration=20.0)
print("Modified Audio Saved Here: ", dist_dir+"/"+file_name+str(10)+".wav")

