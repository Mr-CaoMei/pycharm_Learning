import re

text = ''
file = open("temp913.txt", 'r', encoding="utf-8")
for line in file:
    text = text + line
file.close()
result = re.findall('今天', text)
print(result)
