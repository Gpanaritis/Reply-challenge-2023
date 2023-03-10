f = open("00-example.txt", "r")

line = f.readline()
line = f.readline()
line = line.strip()
snakes = line.split(" ")

f.close()

f = open("00.txt", "r")

output = []
for i in range(len(snakes)):
    output.append([])

used_lines = []
# line = f.readline().strip()

# line = f.readline().strip()
# line = line.split(" ")
# k = int(line[0]) - 3
# print(line)
# print(k)
for j in range(len(snakes)):
    line = f.readline().strip()
    line = line.split(" ")
    k = len(line) - 1
    # print(line)
    # print(k)
    # print(line)
    for i in range(len(snakes)):
        if k == int(snakes[i]) and i not in used_lines:
            # print(i,line)
            output[i].append(line)
            used_lines.append(i)
            break
for o in output:
    for l in o[0]:
        print(l, end=" ")
    print()
f.close()
    
