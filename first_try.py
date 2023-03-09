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