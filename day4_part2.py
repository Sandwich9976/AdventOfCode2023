import re


file = open("day4_data.txt", "r")
text = file.read()
text = re.split("\n", text)
card_count = []
for i in range(0, len(text)):
    card_count.append(1)

for i in range(0, len(text)):
    win = 0
    line2 = re.split("   |  |,|;|:| ", text[i])
    for j in range(14, len(line2)):
        for k in range(3, 14):
            if line2[j] == line2[k]:
                win += 1
    i2 = i+win
    if i2 > len(text):
        i2 = len(text)
    for j in range(i, i2):
        card_count[j+1] += card_count[i]

total = 0
for i in range(0, len(text)):
    total += card_count[i]

print(total)
