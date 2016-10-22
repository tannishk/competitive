def unique(st):
    k = {}
    for i in st:
        k[i]=1
    return len(k.keys())
t = int(raw_input())
while t:
    st = raw_input()
    uni = int(raw_input())
    count = 0
    for j in range(0,len(st)):
        for k in range(j+1,len(st)+1):
            n = unique(st[j:k])
            if(n==uni):
                count=count+1
    print count
    t=t-1
