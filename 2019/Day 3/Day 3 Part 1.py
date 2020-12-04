import re as regex

# open file and extract each move with regex for each wire (line)
with open('input.txt', 'r') as source:
	moves1 = regex.findall(r'(.)(\d+),', source.readline())
	moves2 = regex.findall(r'(.)(\d+),', source.readline())

# each set represents the (x, y) points each wire crosses
points1 = [(0, 0)]
points2 = [(0, 0)]

moves = {
	'U': (0, 1),
	'D': (0, -1),
	'L': (-1, 0),
	'R': (1, 0)
}

# determine all the points the first wire crosses
for move in moves1:
	char, count = move

	lastMove = points1[len(points1) - 1]
	dX, dY = moves[char]

	for i in range(int(count)):
		newPoint = (lastMove[0] + dX*(i+1), lastMove[1] + dY*(i+1))
		points1.append(newPoint)

# determine all the points the second wire crosses
for move in moves2:
	char, count = move

	lastMove = points2[len(points2) - 1]
	dX, dY = moves[char]

	for i in range(int(count)):
		newPoint = (lastMove[0] + dX*(i+1), lastMove[1] + dY*(i+1))
		points2.append(newPoint)

print("Point lists assembled. Comparing...")

intersections = list(set(points1) & set(points2))
intersections.remove((0, 0))
print("Intersections computed. Computing shortest distance...")

shortestDistance = min(abs(x) + abs(y) for (x,y) in intersections)
print('Shortest distance is: ' + str(shortestDistance))