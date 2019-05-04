import math
flag = 0
num = int(input("Input a integer: "))
for i in range (2, int(math.sqrt(num))) :
    if num % i == 0 :
        flag = 1
        break
if flag == 0 :
    print(1)
else :
    print(0)
