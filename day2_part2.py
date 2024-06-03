import re


file = open("day2_data.txt", "r")
text = file.read()
text = re.split("\n", text)
summary = 0

for line in text:
    red_min = 0
    blue_min = 0
    green_min = 0
    line2 = re.split(" |,|;|:", line)
    for i in range(0, len(line2)):
        if line2[i] == 'red':
            if int(line2[i - 1]) > red_min:
                red_min = int(line2[i - 1])
        if line2[i] == 'blue':
            if int(line2[i - 1]) > blue_min:
                blue_min = int(line2[i - 1])
        if line2[i] == 'green':
            if int(line2[i - 1]) > green_min:
                green_min = int(line2[i - 1])
    summary += red_min*blue_min*green_min
print(summary)
