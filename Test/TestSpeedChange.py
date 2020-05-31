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
from Utilities import DirectoryManager
from Utilities import FileManager
from EffectsManager import EffectsManager

# source directory
source_dir = "../../Test_Data/Reference_Audios"
# dis directory
dist_dir = "../../Test_Data/Query_Audios/Speed_Change"
# all reference audios, .mp3 format
mp3_files = DirectoryManager.find_mp3_files(source_dir=source_dir)
# apply speed change on the first audio file
original_audio_path = mp3_files[0]
print(original_audio_path.split("/"))
audio_name = original_audio_path.split("/")[4].split(".")[0]
# modified and original audio paths
print("Original Audio Path: ", original_audio_path)
# applying 10% speed change to for an audio portion specified with offset and duration parameters
speed_change_in_percent = 0
EffectsManager.apply_speed_change(original_audio_path=original_audio_path,
                                  modified_audio_path=dist_dir + "/" + audio_name + "_Speed_" + str(speed_change_in_percent) + ".wav",
                                  target_speed_in_percent=speed_change_in_percent,
                                  offset=10.0,
                                  duration=5.0
                                  )
# applying -10% speed change to an audio portion specified with offset and duration parameters
'''EffectsManager.apply_speed_change(original_audio_path=original_audio_path,
                                  modified_audio_path=dist_dir + "/" + audio_name + str(100 - 10) + ".wav",
                                  target_speed_in_percent=-10,
                                  offset=10.0,
                                  duration=40.0
                                  )'''
