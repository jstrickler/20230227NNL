import os
from datetime import datetime

start_dir = "."
minimum_size = 1500

for folder, sub_folders, file_names in os.walk(start_dir):
    for file_name in file_names:
        if file_name.endswith('.py'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            raw_timestamp = os.path.getmtime(file_path)
            file_timestamp = datetime.fromtimestamp(raw_timestamp)
            file_timestamp_str = file_timestamp.strftime("%x %X")
            if file_size > minimum_size:
                print(f"    {file_size:6d} {file_timestamp_str} {file_path}")



