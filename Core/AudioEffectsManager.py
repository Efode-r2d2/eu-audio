"""
    : AudioEffectsManager
    Author: Efode
    Date: November, 2019
"""
from Utilities import AudioManager
from Utilities import FileManager
from Utilities import DirectoryManager
from Effects import AudioEffects


class EffectManager(object):
    def __init__(self, directory_path=None, file_path=None):
        self.directory_path = directory_path
        self.file_path = file_path

    def apply_speed_change(self, percent, mode=1):
        pass
