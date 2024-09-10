import re

file = open("day11_data.txt", "r")
text = file.read()
text = re.split("\n", text)
data = []
for line in text:
    data.append(line)
empty_col = []
empty_row = []
new_row = 0
new_col = 0
for i in range(len(data)):
    empty_row.append(0)
for i in range(len(data[0])):
    empty_col.append(0)

# finding the number of empty columns and rows
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == ".":
            empty_row[i] += 1
            empty_col[j] += 1
    if empty_row[i] == len(data[i]):
        print(f"empty row {i}")
        new_row += 1

for i in range(len(data[0])):
    if empty_col[i] == len(data[0]):
        print(f"empty col {i}")
        new_col += 1

data2 = []
for i in range(len(data)):
    row = []
    for j in range(len(data[0])):
        row.append(".")
    data2.append(row)

multi = 1000000
coord_row = []
coord_col = []
skip_row = 0
for i in range(len(data)):
    skip_col = 0
    if empty_row[i] == len(data[0]):
        skip_row += 1
    for j in range(len(data[0])):
        if empty_col[j] == len(data):
            skip_col += 1
        if data[i][j] == "#":
            #adding -1 because we jump, for example, from 3 to 12 and without -1 next would be 14 instead of 13
            coord_row.append(i - 1 * skip_row + skip_row * multi)
            coord_col.append(j - 1 * skip_col + skip_col * multi)

summary = 0
for i in range(len(coord_row) - 1):
    for j in range(i, len(coord_col)):
        # finding result. We can use L-shaped lines because there is no straight lines from point A to point B
        sum_1 = abs(coord_row[i] - coord_row[j]) + abs(coord_col[i] - coord_col[j])
        sum_2 = abs(coord_row[j] - coord_row[i]) + abs(coord_col[j] - coord_col[i])
        if sum_1 < sum_2:
            summary += sum_1
        else:
            summary += sum_2

print(summary)
