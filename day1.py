import re


file = open("day1_data.txt", "r")
text = file.read()
text = re.split("\n", text)
summary = 0
for line in text:
    leftnum = "0"
    rightnum = "0"
    for i in range(0, len(line)):
        if line[i] == "0" or line[i] == "1" or line[i] == "2" or line[i] == "3" or line[i] == "4" or line[i] == "5" or line[i] == "6" or line[i] == "7" or line[i] == "8" or line[i] == "9":
            if leftnum == "0":
                leftnum = line[i]
            else:
                rightnum = line[i]
    if rightnum == "0":
        rightnum = leftnum
    summary += int(leftnum)*10+int(rightnum)
    print(line, " ", leftnum, rightnum)
print(summary)
