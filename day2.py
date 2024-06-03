import re


file = open("day2_data.txt", "r")
text = file.read()
text = re.split("\n", text)
summary = 0

for line in text:
    fail = False
    line2 = re.split(" |,|;|:", line)
    for i in range(0, len(line2)):
        if line2[i] == 'red':
            if int(line2[i-1]) > 12:
                fail = True
        if line2[i] == 'green':
            if int(line2[i - 1]) > 13:
                fail = True
        if line2[i] == 'blue':
            if int(line2[i - 1]) > 14:
                fail = True
    if fail is False:
        summary += int(line2[1])
print(summary)
