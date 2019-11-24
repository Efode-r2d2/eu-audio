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


def find_mp3_files(source_dir):
    """

    :type source_dir: object
    """
    mp3_files = []
    for r, d, f in os.walk(source_dir):
        for file in f:
            if '.mp3' in file:
                mp3_files.append(os.path.join(r, file))
    return mp3_files


def find_wav_files(source_dir):
    """

    :type source_dir: object
    """
    wav_files = []
    for r, d, f in os.walk(source_dir):
        for file in f:
            if '.wav' in file:
                wav_files.append(os.path.join(r, file))
    return wav_files


def create_dir(source_dir):
    """

    :type source_dir: object
    """
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
