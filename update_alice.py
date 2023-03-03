"""
Copy alice.txt with substitutions

open alice.txt for input
open temp.txt for output
for line in alice.txt
   for old, new in update_list
       line = line.replace(old, new)
   temp.write(line)

Profiling:
python -m profile -s COLUMN-NAME myscript.txt
python -m profile -o FILE-NAME myscript.txt

python -m pstats FILE-NAME


"""
import os

update_list = [
    ('Alice', 'Betsy'),
    ('rabbit', 'wombat'),
    ('pig', 'wolverine'),
    ('Lizard', 'Godzilla'),
]

INPUT_FILE = 'DATA/alice.txt'

def main():

    num_lines = get_file_size(INPUT_FILE)
    make_replacements(INPUT_FILE, 'temp.txt', update_list, num_lines)

def get_file_size(file_name):
    with open(file_name) as file_in:
        line_count = 0
        for line in file_in:
            line_count += 1
    return line_count

def make_replacements(input_name, output_name, update_list, line_count, *, show_progress=True):
    with open(input_name) as file_in:
        with open(output_name, 'w') as temp_out:
            for line_number, line in enumerate(file_in, 1):  # read one line
                for old_text, replacement in update_list:
                    line = line.replace(old_text, replacement)
                temp_out.write(line)
                if show_progress and (line_number % 100 == 0):
                    percentage = (line_number / line_count) * 100
                    print(f"processed {line_number} input lines ({percentage:.0f}%)")

if __name__ == '__main__':
    main()
