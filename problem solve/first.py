dct = {}
for i in range(int(input())):
    a,b = map(int,input().split())
    dct[a] = dct.get(a,0)+1
    dct[b] = dct.get(b,0)-1
cnt = curr = y = 0
for i in sorted(dct.keys()):
    curr += dct[i]
    if curr > cnt :
        cnt = curr
        y = i
print(y,cnt)
