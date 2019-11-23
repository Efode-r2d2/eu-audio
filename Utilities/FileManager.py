"""
    : FileManager
    Author: Efode
    Date: November, 2019
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
