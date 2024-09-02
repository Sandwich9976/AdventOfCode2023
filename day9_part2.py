import re


def d_matrix(data):
	data.append(0)
	result = []
	for i in range(len(data)):
		zeros = []
		if i == 0:
			result.append(data)
		else:
			for j in range(len(data)):
				zeros.append(0)
			result.append(zeros)
	return result


file = open("day9_data.txt", "r")
text = file.read()
text = re.split("\n", text)
total = 0
fields = []
for word in text:
	words = re.split(" ", word)
	for i in range(len(words)):
		words[i] = int(words[i])
	fields.append(words)
data = [1, 2, 3, 4, 5, 6]
data2 = [10, 13, 16, 21, 30, 45]
for field in fields:
	field = d_matrix(field)
	for i in range(len(field)):
		print(field[i])
	print("____________")
	length = len(field) - 1

	for i in range(0, length):
		for j in range(0, length-i-1):
			field[i+1][j] = field[i][j+1] - field[i][j]

	for i in range(len(field)):
		print(field[i])
	print("_______________")

	for i in range(length-1, -1, -1):
		field[i][length-i] = field[i][0]-field[i+1][length-i-1]

	for i in range(len(field)):
		print(field[i])
	total += field[0][len(field)-1]

print(total)
