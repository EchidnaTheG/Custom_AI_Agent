import os
import sys
from pprint import pprint
def get_files_info(working_directory, directory=None):
    if os.path.isdir(working_directory):
        files_path = os.path.join(working_directory,directory)
        
        print(files_path)
        if os.path.isdir(files_path):
            lst_dir_content = os.listdir(files_path)
            srt_rep_dict = {

            }
            for content in lst_dir_content:
                srt_rep_dict[content] = f"file_size={os.path.getsize(os.path.join(os.path.abspath(working_directory),directory, content))} bytes, is_dir={os.path.isdir(os.path.join(os.path.abspath(working_directory),directory, content))}"
            return srt_rep_dict
#print(get_files_info("calculator", "."))
#print(get_files_info("calculator", "pkg"))
print(get_files_info("calculator", "/bin"))
#pprint(get_files_info("calculator", "../"))