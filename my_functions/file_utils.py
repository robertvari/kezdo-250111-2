import os

def find_files(root_folder, file_list):
    assert os.path.isdir(root_folder), f"{root_folder} if not a directory."








# this runs only if file_utils.py being run
if __name__ == "__main__":
    root_folder = r"C:\Work\Houdini"
    file_list = []
    find_files(root_folder, file_list)