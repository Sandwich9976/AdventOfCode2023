import re


file = open("day4_data.txt", "r")
text = file.read()
text = re.split("\n", text)
total = 0.0

for line in text:
    line2 = re.split("   |  |,|;|:| ", line)
    score = 0.5
    print(line2[3:13],line2[14:len(line2)])
    for i in range(14, len(line2)):
        for j in range(3, 14):
            if line2[i] == line2[j]:
                score = score * 2
    if score >= 1:
        total += score

print(total)
