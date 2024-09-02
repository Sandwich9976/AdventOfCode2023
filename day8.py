import re

# file import
file = open("day8_data.txt", "r")
text = file.read()
text = re.split("\n", text)
#print(text)
pattern = text[0]
path = []
left = []
right = []
i = 0
for word in text:
    trail = re.split(" = .|, |.$", word)
    i += 1
    if i > 2:
        path.append(trail[0])
        left.append(trail[1])
        right.append(trail[2])

#for i in range(0, len(path)):
    #print(path[i], "= (", left[i], ", ", right[i], ")")

current_node = "AAA"
finish = False
step = 0
count = 0

while finish is False:
    if current_node == "ZZZ":
        finish = True
    for i in range(0, len(path)):
        if path[i] == current_node:
            if pattern[step] == "L":
                print(current_node, "moved to", left[i])
                current_node = left[i]
                step += 1
                count += 1
            else:
                print(current_node, "moved to", right[i])
                current_node = right[i]
                step += 1
                count += 1
            if step >= len(pattern):
                print("step retured to 0")
                step = 0
            if current_node == "ZZZ":
                finish = True
                print(count)
                exit()
