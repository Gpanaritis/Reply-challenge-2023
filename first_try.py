def down(i,j):
    if i < rows-1:
        if system[i+1][j] == "*":
            return
        else:
            return i+1,j,int(system[i+1][j])
    elif i == rows-1:
        return 0,j,int(system[0][j])

def up(i,j):
    if i > 0:
        if system[i-1][j] == "*":
            return
        else:
            return i-1,j,int(system[i-1][j])
    elif i == 0:
        return rows-1,j,int(system[rows-1][j])

def right(i,j):
    if j < columns-1:
        if system[i][j+1] == "*":
            return
        else:
            return i,j+1,int(system[i][j+1])
    elif j == columns-1:
        return i,0,int(system[i][0])

def left(i,j):
    if j > 0:
        if system[i][j-1] == "*":
            return
        else:
            return i,j-1,int(system[i][j-1])
    elif j == 0:
        return i,columns-1,int(system[i][columns-1])

f = open("00-example.txt", "r")

line = f.readline()

line = line.strip()

line = line.split(" ")

columns = int(line[0])
rows = int(line[1])
num_snakes = int(line[2])

line = f.readline()
snakes = []
line = line.strip()
line = line.split(" ")
snakes = line.copy()

system = []

for i in range(rows):
    system.append([])
    line = f.readline()
    line = line.strip()
    line = line.split(" ")
    for j in range(columns):
        system[i].append(line[j])

print(system)