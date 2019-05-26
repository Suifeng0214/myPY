nn = int(input("Input 3-5-X : "))   # input 3~5
listx=[]
for i in range (0,nn):
    listx.append(chr(65+i))       # Build up working List

print("The combinations for '%s' is following: " % ("".join(listx[0:nn])))    # print List on screen


def rotate(rlist):                    # procedure for rotation
    for i in range(0,len(rlist)-1) :
        rlist[i],rlist[i+1]=rlist[i+1],rlist[i]
    
def perm(wlist,xx):                   # procedure for 排列組合副程式 wlist是遞迴要處理的List  xx是前幾層累積的的字串 
    lenn = len(wlist)
    if lenn ==1 :                              #   if List length == 1 , print
        print(xx+wlist[0])                     # 印前幾層累積的的字串 xx, 再印最後一個             
    else:
        for i in range(0,lenn):
            perm(wlist[1:lenn],xx+wlist[0])    # 保留第一個元素  其餘的LIst 遞迴呼叫perm副程式
                                               # 第一個元素加上上一層帶進來的, 累積組合成字串, 當成第二參數傳進去
            rotate(wlist)                      # 遞迴呼叫後  List 旋轉 

perm(listx,'')                                 # 主程式  一行

print(listx)                                   # 最後檢查原始Lis是否還原