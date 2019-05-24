num = 10000
while (num < 100000):
    temp = num
    Sum = 0
    while(temp * 10 // 10 != 0):
        Sum += (temp % 10) ** len(str(num))
        temp //= 10  
    if Sum == num:
        print(num)
    num += 1
