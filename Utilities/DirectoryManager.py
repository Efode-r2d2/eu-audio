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


class DirectoryManager(object):
    def __init__(self, directory_path):
        self.directory_path = directory_path
    """ 
        Find all .mp3 files with in a given directory
    """
    def find_mp3_files(self):
        mp3_files = []
        for r, d, f in os.walk(self.directory_path):
            for file in f:
                if '.mp3' in file:
                    mp3_files.append(os.path.join(r, file))
        return mp3_files
    """
        Find all .wav files with in a given directory
    """
    def find_wav_files(self):
        wav_files = []
        for r, d, f in os.walk(self.directory_path):
            for file in f:
                if '.wav' in file:
                    wav_files.append(os.path.join(r, file))
        return wav_files
    """
        Creating new directory 
    """
    def create_dir(self):
        if not os.path.exists(self.directory_path):
            os.makedirs(self.directory_path)
