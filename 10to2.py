while (input("Continue the program input 'y'\n") == 'y'):
	num = int(input("Please input an integer: "))
	newNum = ""
	while (num > 0):
		newNum = str(num % 2) + newNum
		num //= 2
	print(newNum)
	
