import os
import re

# get the valutDir from the environment variable
vaultDir = os.environ['VAULTDIR']

file_count = 0
for subdir, dirs, files in os.walk(vaultDir):
    for file in files:
        if ".md" not in file:
            continue
        file_count += 1
        full_file_path = os.path.join(subdir, file)
        with open(full_file_path, 'r', encoding='latin1') as file:
            data = file.read()

        last_indent = None
        for line in data.splitlines():
            if line.startswith("#"):
                last_indent = None
            elif re.search(r"^\s*- ", line):  # bullet point
                indentation = len(line) - len(line.lstrip())
                if last_indent is None:
                    last_indent = indentation
                data = data.replace(line, line[last_indent:])

        with open(full_file_path, 'w', encoding='latin1') as file:
            file.write(data)

        print(f"Converted {file_count}", end="\r")

print(f"Converted {file_count}")