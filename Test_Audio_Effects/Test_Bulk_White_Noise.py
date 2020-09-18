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

# source directory of reference audios
ref_audios_dir = "../../Test_Data/Ref_Audios"
# destination directory of query audios
query_audio_dir = "../../Test_Data/Query_Audios/White_Noise"
# reference audios
reference_audios = directory_manager.find_wav_files(source_dir=ref_audios_dir)
# applying pitch shifting for set of reference audio files
for i in reference_audios:
    audio_name = i.split("/")[4]
    for j in range(-10, 25, 5):
        directory_manager.create_dir(source_dir=query_audio_dir + "/" + str(j))
        effects_manager.add_white_noise(original_audio_path=i,
                                        modified_audio_path=query_audio_dir + "/" + str(j) + "/" + audio_name,
                                        target_snr_in_db=j,
                                        offset=None,
                                        duration=None)
