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
import os
from eyed3 import id3


class FileManager(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def rename_file(self, new_file_path):
        os.rename(self.file_path, new_file_path)

    def get_meta_data(self):
        tag = id3.Tag()
        tag.parse(self.file_path)
        return tag.artist, tag.album, tag.title
