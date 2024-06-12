import re

"""numbers = [1, 2, 3]
total = 0
count = 1
for number in numbers:
    total += number*pow(10, len(numbers)-count)
    count += 1
print(total)"""
dot_count = 0

file = open("day3_data.txt", "r")
text = file.read()
text = re.split("\n", text) #starts from [0][0] and text is 140x140 len
for i in range(0, len(text)):
    number = []
    for j in range(0, len(text[i])):
        fail = False
        if text[i][j] == "1" or text[i][j] == "2" or text[i][j] == "3" or text[i][j] == "4" or text[i][j] == "5" or text[i][j] == "6" or text[i][j] == "7" or text[i][j] == "8" or text[i][j] == "9" or text[i][j] == "0":
            number.append(int(text[i][j]))
        else:
            fail = True
        if fail is True and len(number) > 0 or j == len(text[i])-1:
            mult = 0
            up_wall = i-1
            if up_wall == -1:
                up_wall = 0
            down_wall = i+2
            if down_wall > len(text):
                down_wall = len(text)
            left_wall = j-1-len(number)
            if left_wall < 0:
                left_wall = 0
            right_wall = j+1
            for i2 in range(up_wall, down_wall):
                for j2 in range(left_wall, right_wall):
                    if text[i2][j2] != "1" and text[i2][j2] != "2" and text[i2][j2] != "3" and text[i2][j2] != "4" and text[i2][j2] != "5" and text[i2][j2] != "6" and text[i2][j2] != "7" and text[i2][j2] != "8" and text[i2][j2] != "9" and text[i2][j2] != "0" and text[i2][j2] != ".":
                        mult = 1
            summary = 0
            if len(number) == 3:
                summary = mult * (100 * number[0] + 10 * number[1] + number[2])
            elif len(number) == 2:
                summary = mult * (10*number[0]+number[1])
            elif len(number) == 1:
                summary = mult * (number[0])
            dot_count += summary
            number = []


print(dot_count)
