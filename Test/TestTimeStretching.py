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
from EffectsManager import EffectsManager
from Utilities import DirectoryManager
# source directory
src_dir = "../../Test_Data/Reference_Audios"
# destination directory path for modified audios
dist_dir = "../../Test_Data/Modified_Audios/Time_Stretched"
# find all .mp3 files under given source directory
mp3_files = DirectoryManager.find_mp3_files(source_dir=src_dir)
# applying time stretching to the second audio in .mp3 files list
original_audio_path = mp3_files[1]
file_name = original_audio_path.split("/")[4].split(".")[0]
print("Original Audio Path: ", original_audio_path)
print("File Name", file_name)
# applying 10% time stretching on a portion of audio defined by offset and duration parameters
EffectsManager.apply_time_stretching(original_audio_path=original_audio_path,
                                     modified_audio_path=dist_dir+"/"+file_name+str(100+10)+".wav",
                                     target_duration_in_percent=10,
                                     offset=10.0,
                                     duration=20.0)
print("Audio Saved Here, ", dist_dir+"/"+file_name+str(100+10)+".wav")
# applying -10% time stretching on a portion of audio defined by offset and duration parameters
EffectsManager.apply_time_stretching(original_audio_path=original_audio_path,
                                     modified_audio_path=dist_dir+"/"+file_name+str(100-10)+".wav",
                                     target_duration_in_percent=-10,
                                     offset=10.0,
                                     duration=20.0)
print("Audio Saved Here, ", dist_dir+"/"+file_name+str(100-10)+".wav")


