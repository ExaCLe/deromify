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
        with open(full_file_path, 'r') as file:
            try:
                data = file.read()
            except UnicodeDecodeError:
                continue

        in_definition = False
        for line in data.splitlines():
            definition_start = re.search(r'^\s*- >', line) is not None
            definition_end = re.search(r'^\s*#{1,3}', line) is not None

            if in_definition and definition_end:
                data = data.replace(line, '```\n' + line)
                in_definition = False
            elif definition_start:
                prefix = "```\n" if in_definition else ""
                in_definition = True
                if 'Definition' in line:
                    substitution = '```ad-definition\\ntitle: Definition \g<name>\\n'
                else:
                    substitution = '```ad-satz\\ntitle:\g<name>\\n'
                newLine = re.sub('^\s*- > \*{0,2}(Definition )?(?P<name>[\wäöü ]+)\*{0,2}:\*{0,2}', substitution, line)
                data = data.replace(line, prefix + newLine)

        with open(full_file_path, 'w') as file:
            file.write(data)

        print(f"Converted {file_count}", end="\r")

print(f"Converted {file_count}")