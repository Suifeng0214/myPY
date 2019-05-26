floor = int(input("How many floors you want to build\n"))
tri = [[0] * floor for i in range(floor)]

for i in range(0, floor):
    tri[i][0] = 1
    if(i > 0):
        tri[i][i] = 1

for i in range(2, floor):
    for j in range(1, i):
        tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

for i in range(0, floor):
    for j in range(floor, i-1, -1):
        print("   ", end = "")
    for k in range(0, j+1):
        print("%6d" %( tri[j][k]), end = "")
    print()
