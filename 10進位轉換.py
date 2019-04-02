tenthDg = int(input('請輸入欲轉換之十進位數: '))
tenthdg1 = tenthDg
tenthdg2 = tenthDg

x = 1
digit2 = []
digit8 = []

while (tenthDg // 2) >= 1:
	tenthDg //= 2	
	x += 1
	
for i in range (0, x+1):
    digit2.append(0)
    digit8.append(0)
	
for j in range (x, 0, -1):
    digit2[j] = tenthdg1 % 2
    tenthdg1 //= 2

for k in range (x, 0, -1):
    digit8[k] = tenthdg2 % 8
    tenthdg2 //= 8
    
print('二進位轉換: ',digit2)
print('八進位轉換: ',digit8)

