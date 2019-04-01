a = [0,1]
for j in range (2,100):
    a.append(a[j-1] + a[j-2])
    if a[j] <= 1000:
        print(a[j])
    else:
        break
