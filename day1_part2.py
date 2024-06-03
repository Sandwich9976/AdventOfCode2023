import re


file = open("day1_data.txt", "r")
text = file.read()
text = re.split("\n", text)
summary = 0
for line in text:
    #trying to convert words into numbers, remembering that one letter may be shared between two words
    #Though this leads into problem: Might exist a loop of 8-3-2-1-8-3-2-1 or 8-3-8-3-8-3...
    line = re.sub("oneight", "18", line)
    line = re.sub("twone", "21", line)
    line = re.sub("threeight", "38", line)
    line = re.sub("fiveight", "58", line)
    line = re.sub("sevenine", "79", line)
    line = re.sub("eightwo", "82", line)
    line = re.sub("eighthree", "83", line)
    line = re.sub("nineight", "98", line)
    line = re.sub("one", "1", line)
    line = re.sub("two", "2", line)
    line = re.sub("three", "3", line)
    line = re.sub("four", "4", line)
    line = re.sub("five", "5", line)
    line = re.sub("six", "6", line)
    line = re.sub("seven", "7", line)
    line = re.sub("eight", "8", line)
    line = re.sub("nine", "9", line)
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
#took 6 attempts to get right answer
