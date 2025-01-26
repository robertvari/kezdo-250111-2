import os

def find_files(root_folder: str, file_list: list, filter=None):
    # check if rooot_folder is a valid folder
    assert os.path.isdir(root_folder), f"{root_folder} is not a directory."
    # check if file_list is a list
    assert isinstance(file_list, list), "file_list must be a list."

    # collect content of the root_folder
    folder_content = os.listdir(root_folder)

    # create a container for subfolders
    subfolders = []

    # step through of folder_content and collect files and subfolders
    for i in folder_content:
        # create a valid path (absolute path) to the file/folder
        full_path = os.path.join(root_folder, i)

        # check if the full_path is a file
        if os.path.isfile(full_path):
            # store file in file_list
            if filter:  # check if we have filter
                if filter in full_path:  # check if filter part of the full_path
                    file_list.append(full_path)
            else:
                file_list.append(full_path)
        else:  # this is a subfolder so I store it in subfolders
            subfolders.append(full_path)


    # recursive call if we found subfolders
    for folder in subfolders:
        find_files(folder, file_list, filter)


# this runs only if file_utils.py being run
if __name__ == "__main__":
    root_folder = r"C:\Work\Houdini"
    file_list = []
    find_files(root_folder, file_list, filter=".ini")

    for i in file_list:
        print(i)
    
    print(f"We found {len(file_list)} files")