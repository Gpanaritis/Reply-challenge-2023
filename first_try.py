def get_max_index(system):
    max_val = 0
    max_pos = [0,0]
    for i in range(len(system)):
        for j in range(len(system[i])):
            if system[i][j] == "*":
                continue
            elif int(system[i][j]) > max_val and occupied[i][j] == False:
                max_val = int(system[i][j])
                max_pos = [i,j]
                
    return max_pos

def down(i,j):
    if i < rows-1:
        if system[i+1][j] == "*":
            return
        else:
            return i+1,j,int(system[i+1][j]),occupied[i+1][j]
    elif i == rows-1:
        return 0,j,int(system[0][j]),occupied[0][j]

def up(i,j):
    if i > 0:
        if system[i-1][j] == "*":
            return
        else:
            return i-1,j,int(system[i-1][j]),occupied[i-1][j]
    elif i == 0:
        return rows-1,j,int(system[rows-1][j]),occupied[rows-1][j]

def right(i,j):
    if j < columns-1:
        if system[i][j+1] == "*":
            return
        else:
            return i,j+1,int(system[i][j+1]),occupied[i][j+1]
    elif j == columns-1:
        return i,0,int(system[i][0]),occupied[i][0]

def left(i,j):
    if j > 0:
        if system[i][j-1] == "*":
            return
        else:
            return i,j-1,int(system[i][j-1]),occupied[i][j-1]
    elif j == 0:
        return i,columns-1,int(system[i][columns-1]),occupied[i][columns-1]

f = open("00-example.txt", "r")

line = f.readline()

line = line.strip()

line = line.split(" ")

columns = int(line[0])
rows = int(line[1])
num_snakes = int(line[2])

snakes = []
warmholes = []
occupied = []

line = f.readline()
line = line.strip()
line = line.split(" ")
snakes = line.copy()

system = []

for i in range(rows):
    system.append([])
    occupied.append([])
    line = f.readline()
    line = line.strip()
    line = line.split(" ")
    for j in range(columns):
        system[i].append(line[j])
        occupied[i].append(False)
        if line[j] == "*":
            warmholes.append([i,j])

# get max index from system
max_idx = get_max_index(system)
print(max_idx)