from Utilities import DirectoryManager
from Utilities import FileManager
from EffectsManager import EffectsManager

# define the path for source directory
source_dir = "../../Test_Data/Reference_Audios"
# search for all .mp3 files under the specified source directory
mp3_files = DirectoryManager.find_mp3_files(source_dir=source_dir)
for i in mp3_files:
    # printing meta data for each mp3 file
    print(FileManager.get_meta_data(i), i)
