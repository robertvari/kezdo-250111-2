from my_functions.file_utils import find_files

root_folder = r"C:\Work\Houdini"
file_list = []
find_files(root_folder, file_list, filter=".jpg")

for i in file_list:
    print(i)
print(f"We found {len(file_list)} files")