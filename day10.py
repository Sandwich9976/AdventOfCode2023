import re
import sys
#python limits recursions pretty heavily
sys.setrecursionlimit(25000)
file = open("day10_data.txt", "r")
text = file.read()
text = re.split("\n", text)
pipeline = []
for line in text:
	pipeline.append(line)
moves = 0


def move_up(i, j):
	global moves
	moves+=1
	match(pipeline[i-1][j]):
		case("|"):
			move_up(i-1, j)
		case("7"):
			move_left(i-1, j)
		case("F"):
			move_right(i-1,j)


def move_down(i, j):
	global moves
	moves+=1
	match(pipeline[i+1][j]):
		case("|"):
			move_down(i+1, j)
		case("J"):
			move_left(i+1, j)
		case("L"):
			move_right(i+1,j)


def move_left(i, j):
	global moves
	moves+=1
	match(pipeline[i][j-1]):
		case("-"):
			move_left(i, j-1)
		case("L"):
			move_up(i, j-1)
		case("F"):
			move_down(i,j-1)


def move_right(i, j):
	global moves
	moves+=1
	match(pipeline[i][j+1]):
		case("-"):
			move_right(i, j+1)
		case("J"):
			move_up(i, j+1)
		case("7"):
			move_down(i, j+1)


for i in range(len(pipeline)):
	for j in range(len(pipeline[i])):
		if pipeline[i][j] == "S":
			move_down(i, j)
			print(moves)
			if moves <= 1:
				moves = 0
				move_left(i, j)
			if moves <= 1:
				moves = 0
				move_right(i, j)
			if moves <= 1:
				moves = 0
				move_up(i, j)
			print("shortest path is in moves: ", moves/2)
			