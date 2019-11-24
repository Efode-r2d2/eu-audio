from Utilities import DirectoryManager
from Utilities import FileManager
from EffectsManager import EffectsManager

# define the path for source directory
source_dir = "../../Test_Data/Reference_Audios"
# define destination path for modified audios
dist_dirc = "../../Test_Data/Modified_Audios/Speed_Change"
# search for all .mp3 files under the specified source directory
mp3_files = DirectoryManager.find_mp3_files(source_dir=source_dir)
# apply speed change on the first audio file
original_audio_path = mp3_files[0]
print(original_audio_path.split("/"))
audio_name = original_audio_path.split("/")[4].split(".")[0]
# modified and original audio paths
print("Original Audio Path: ", original_audio_path)
# applying 10% speed change to for an audio portion specified with offset and duration parameters
EffectsManager.apply_speed_change(original_audio_path=original_audio_path,
                                  modified_audio_path=dist_dirc+"/"+audio_name+str(100+10)+".wav",
                                  target_speed_in_percent=10,
                                  offset=10.0,
                                  duration=20.0
                                  )
# applying -10% speed change to an audio portion specified with offset and duration parameters
EffectsManager.apply_speed_change(original_audio_path=original_audio_path,
                                  modified_audio_path=dist_dirc+"/"+audio_name+str(100-10)+".wav",
                                  target_speed_in_percent=-10,
                                  offset=10.0,
                                  duration=20.0
                                  )

