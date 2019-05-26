import random                                    # 引入亂數函數

# x & list01 先定義  x 和 list01  空串列使用的位置相同 ，其實是同一個 串列
x=list01=[]

for i in range(1,11):
    a=random.randint(1,100)
    list01.append(a)                             # 附加元素
    print(a)
print(x)                                         # 印出 x

print('由小到大排列為 ',sorted(x))               # 用函數快又簡單 
print('由大到小排列為 ',sorted(x,reverse=True))  # 用函數，反排 

for p in range(0,10):                    
    # list01[P]                                  # 這一行多餘
    for h in range(2,list01[p]):                 # 可用 range(2,list01[p]//2+1)) 
        if (list01[p] % h)==0:                   # 或用 range(2,int(list01[p]**0.5)+1)，引數需整數
           # print(list01[p],'不是質數')
            break                                # 有一個被廚進就終止 跳出
    else:
        print('%3d' %list01[p],' 是質數')        # 沒有被除盡過，就是質數
