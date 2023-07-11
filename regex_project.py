import re
with open('regex_test.txt') as f:
    data = f.readlines()

pattern = re.compile("([A-Z][\w]+) (\w)+")
for line in data:
    match = pattern.search(line)
    if match:
        print(line)
    else:
        print('None\n')