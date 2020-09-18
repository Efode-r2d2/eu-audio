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
from Utilities import file_manager

# file path
file_path = "../../Test_Data/Reference_Audios/Audio1.mp3"
"""
get metadata, get_meta_data will return a list which contains metadata 
about the audio located in a given path
"""
file_meta_data = file_manager.get_meta_data(file_path=file_path)
# print metadata
print(file_meta_data)
