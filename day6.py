import re

file = open("day6_data.txt", "r")
text = file.read()
text = re.split("\n", text)
words = []
for word in text:
    word = re.split("        |       |       |      |     |    |   |  | ", word)
    words.append(word)
result = 1
for i in range(1, 5):
    passed = 0
    limit = int(words[0][i])
    treshold = int(words[1][i])
    for j in range(0, limit+1):
        number = j * (limit-j)
        if number > treshold:
            passed += 1
    result *= passed
print(result)
