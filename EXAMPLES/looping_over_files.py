import sys

files_to_open = sys.argv[1:]
for file_path in files_to_open:  # skip script name
    print(f"Processing {file_path}")
    with open(file_path) as file_in:
        pass   #  read each file here

# cf.  fileinput module