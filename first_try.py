def find_max_path(i,j,threshold):
    counter = 0
    visited = []

    occupied[i][j] = True
    visited.append([i,j])
    for k in range(int(snakes[0]) - 1):
        max_neighbour = get_max_neighbour(i,j)
        if max_neighbour[2] > threshold:
            counter += 1
            visited.append(max_neighbour)
            if type(max_neighbour[1]) == list:
                k += 1
            i,j = max_neighbour[0]
            occupied[i][j] = True
        if ( max_neighbour[2] < threshold ):
            pass
    return visited
        


        

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

def get_max_neighbour(i,j):
    up_val = up(i,j)
    down_val = down(i,j)
    left_val = left(i,j)
    right_val = right(i,j)
    max_val = 0
    max_type = ""

    if up_val[2] != '*':
        if up_val[2] > max_val and up_val[3] == False:
            max_val = up_val[2]
            max_pos = up_val[0],up_val[1]
            max_type = "U"
    elif up_val[2] == '*' :
        for w in warmholes:
            max_pos_temp,max_type_temp,max_val_temp = get_max_neighbour(w[0],w[1])
            if max_val_temp > max_val:
                max_val = max_val_temp
                max_pos = max_pos_temp
                max_type = ['U', max_type_temp]

    if down_val[2] != '*':
        if down_val[2] > max_val and down_val[3] == False:
            max_val = down_val[2]
            max_pos =  down_val[0],down_val[1]
            max_type = "D"
    elif down_val[2] == '*' :
        for w in warmholes:
            max_pos_temp,max_type_temp,max_val_temp = get_max_neighbour(w[0],w[1])
            if max_val_temp > max_val:
                max_val = max_val_temp
                max_pos = max_pos_temp
                max_type = ['D', max_type_temp]
    if left_val[2] != '*':
        if left_val[2] > max_val and left_val[3] == False:
            max_val = left_val[2]
            max_pos = left_val[0],left_val[1]
            max_type = "L"
    elif left_val[2] == '*' :
        for w in warmholes:
            max_pos_temp,max_type_temp,max_val_temp = get_max_neighbour(w[0],w[1])
            if max_val_temp > max_val:
                max_val = max_val_temp
                max_pos = max_pos_temp
                max_type = ['L', max_type_temp]
    if right_val[2] != '*':
        if right_val[2] > max_val and right_val[3] == False:
            max_val = right_val[2]
            max_pos = right_val[0],right_val[1]
            max_type = "R"
    elif right_val[2] == '*':
        for w in warmholes:
            max_pos_temp,max_type_temp,max_val_temp = get_max_neighbour(w[0],w[1])
            if max_val_temp > max_val:
                max_val = max_val_temp
                max_pos = max_pos_temp
                max_type = ['R', max_type_temp]
    
    return max_pos,max_type,max_val
    

def down(i,j):
    if i < rows-1:
        if system[i+1][j] == "*":
            return i+1,j,'*',False
        else:
            return i+1,j,int(system[i+1][j]),occupied[i+1][j]
    elif i == rows-1:
        return 0,j,int(system[0][j]),occupied[0][j]

def up(i,j):
    if i > 0:
        if system[i-1][j] == "*":
            return i-1,j,'*',False
        else:
            return i-1,j,int(system[i-1][j]),occupied[i-1][j]
    elif i == 0:
        return rows-1,j,int(system[rows-1][j]),occupied[rows-1][j]

def right(i,j):
    if j < columns-1:
        if system[i][j+1] == "*":
            return i,j+1,'*',False
        else:
            return i,j+1,int(system[i][j+1]),occupied[i][j+1]
    elif j == columns-1:
        return i,0,int(system[i][0]),occupied[i][0]

def left(i,j):
    if j > 0:
        if system[i][j-1] == "*":
            return i,j-1,'*',False
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

snakes = sorted(snakes, key=int, reverse=True)

# get max index from system
# pos = get_max_index(system)
# pos = get_max_neighbour(0,0)
# print(pos)
k = len(snakes)
v = []
for k in range(k):
    i,j = get_max_index(system)
    visited = find_max_path(i,j,0)
    # remove first snake
    snakes.pop(0)
    v.append(visited)

for i in range(len(v)):
    for j in range(len(v[i])):
        if j == 0:
            print(v[i][j][0],v[i][j][1],end=" ")

        elif type(v[i][j][1]) == str:
            print(v[i][j][1], end = " ")

        elif type(v[i][j][1]) == list:
            # print(type(v[i][j][1]))
            print(v[i][j][1][0],v[i][j][0][1],v[i][j][0][0], v[i][j][1][1], end = " ")
    print()
