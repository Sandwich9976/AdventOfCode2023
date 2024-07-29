import re

file = open("day6_data.txt", "r")
text = file.read()
text = re.split("\n", text)
words = []
for word in text:
    word = re.split("        |       |       |      |     |    |   |  | ", word)
    words.append(word)
result = 1
for i in range(2, 5):
    words[0][1] += words[0][i]
    words[1][1] += words[1][i]
print(words[0][1], words[1][1])


passed = 0
limit = int(words[0][1])
treshold = int(words[1][1])
for j in range(0, limit+1):
    number = j * (limit-j)
    if number > treshold:
        passed += 1
result *= passed
print(result)
