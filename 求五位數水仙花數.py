for i in range(10000, 100000):
        num = int(input("Check the number: "))
        temp = num
        Sum = 0
        while(temp * 10 // 10 != 0):
            Sum += (temp % 10) ** len(str(num))
            temp //= 10  
        if Sum == num:
            print(1)
        else:
        	print(0)
