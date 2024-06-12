import re

dot_count = 0
number_many = []
file = open("day3_data.txt", "r")
text = file.read()
text = re.split("\n", text)  # starts from [0][0] and text is 140x140 len
for i in range(0, len(text)):
    for j in range(0, len(text[i])):
        if text[i][j] == "*":
            number = ""
            numbers = []
            up_wall = i - 1
            down_wall = i + 2
            if down_wall > 140:
                down_wall = 140
            left_wall = j - 1
            if left_wall < 0:
                left_wall = 0
            right_wall = j + 1
            for i2 in range(up_wall, down_wall):
                left = left_wall
                match text[i2][left_wall]:
                    case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
                        left -= 1
                        match text[i2][left_wall-1]:
                            case '.' | '+' | '-' | "/" | '=' | '*' | '@' | '$' | '%' | '&':
                                pass
                            case _:
                                left -= 1
                right = right_wall+1
                match text[i2][right_wall]:
                    case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
                        match text[i2][right_wall+1]:
                            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
                                right += 2
                for j2 in range(left, right):
                    match text[i2][j2]:
                        case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
                            number += text[i2][j2]
                        case _:
                            if len(number) > 0:
                                numbers.append(int(number))
                                number = ""
                    if j2 == right-1 and len(number) > 0:
                        numbers.append(int(number))
                        number = ""
            print("found * in:", i, j, "numbers are:",numbers)
            if len(numbers) == 2:
                number_many.append(numbers)

total = 0
print(number_many)
for number in number_many:
    total += number[0] * number[1]

print(total) #This riddle broke my head for a couple of times tbh...
