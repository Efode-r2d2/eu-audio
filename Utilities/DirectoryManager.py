"""
    Class Name: DirectoryManager
    Author: Efriem Desalew, efidesalew@gmail.com
    Date: November, 2019
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
