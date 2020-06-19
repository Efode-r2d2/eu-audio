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
from Utilities import AudioManager
from EffectsManager import EffectsManager

# directory path for full length reference audios
source_dir = "../../Test_Data/Reference_Audios"
# directory path for short snippet reference audios
dist_dir = "../../Test_Data/Ref_Audios/"
# reference audios
reference_audios = DirectoryManager.find_mp3_files(source_dir=source_dir)
for i in reference_audios[0:10]:
    audio_name = i.split("/")[4].split(".")[0]
    # reading only 5 second audio duration
    audio_excerpt, sr = AudioManager.load_audio(audio_path=i, offset=10.0, duration=5.0)
    # saving the 5 second audio duration
    AudioManager.save_audio(audio_path=dist_dir + audio_name + ".wav", audio_data=audio_excerpt, sr=sr)
