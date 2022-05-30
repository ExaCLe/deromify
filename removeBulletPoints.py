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

        expression = re.compile(r"^(?P<space>\s*)- (?P<hash>#{1,3})", re.MULTILINE)
        data = re.sub(expression, r"\g<hash>", data)

        with open(full_file_path, 'w', encoding='latin1') as file:
            file.write(data)

        print(f"Converted {file_count}", end="\r")

print(f"Converted {file_count}")