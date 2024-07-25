import re

file = open("day5_data.txt", "r")
text = file.read()
text = re.split("\n", text)
words = []
for word in text:
    word = re.split(" ", word)
    words.append(word)
numbers = []
checks = []

# get seeds (range from one because 'seeds:' take index 0)
for i in range(1, len(words[0])):
    numbers.append(int(words[0][i]))
    checks.append("true")

print(numbers)

for i in range(1, len(words)):
    # could do with [i][1] instead, but it leads to indexing error from blank strings
    match (words[i][0]):
        case ("seed-to-soil" | "soil-to-fertilizer" | "fertilizer-to-water" | "water-to-light" | "light-to-temperature" | "temperature-to-humidity" | "humidity-to-location"):
            for j in range(0, len(numbers)):
                checks[j] = "false"
            k = 1
            while words[i + k][0] != '':
                for j in range(0, len(numbers)):
                    a = int(words[i + k][0])
                    b = int(words[i + k][1])
                    c = int(words[i + k][2])
                    if b <= numbers[j] < (b + c):
                        if checks[j] == 'false':
                            numbers[j] = a - b + numbers[j]
                            checks[j] = 'true'
                k += 1

print(numbers)
print(min(numbers))
