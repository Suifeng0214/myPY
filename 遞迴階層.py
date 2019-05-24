def stair(x):
	if x == 1:
		return x
	else:
		return x * stair(x-1)
	
num = int(input("Find n! \nn = "))
temp = stair(num)
numSum = 0
numLen = len(str(stair(num)))
while (temp * 10 // 10 != 0):
	numSum = numSum + (temp % 10)
	temp //= 10
print(num, "! = ", stair(num))
print("numLen = ", len(str(stair(num))))
print("numSum = ", numSum)

