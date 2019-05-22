num = int(input("Please input an integer:\n"))
tempNum = num
reNum = 1
start = 2

print(num,"= ", end = "")
while reNum < num :
	while tempNum % start == 0 :
		if reNum == 1:
			print(start,end = "")
		else:
			print(" x", start,end = "")
		tempNum //= start
		reNum *= start
	start += 1
