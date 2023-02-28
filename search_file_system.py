import os
start_dir = "C:\\"
file_to_find = "presidents.txt"

for folder, sub_folders, file_names in os.walk(start_dir):
    if '.git' in sub_folders:
        sub_folders.remove('.git')
    for file_name in file_names:
        if file_name == file_to_find:
            file_path = os.path.join(folder, file_name)
            print(file_path)
