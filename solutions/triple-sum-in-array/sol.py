t = int(raw_input())
res = 0

while t>0:
    dict={}
    res=0
    n,x = map(int,raw_input().split())
    arr = map(int,raw_input().split())
    arr.sort()
    for i in arr:
        dict[i]=True
    for i in range(0,n-2):
        if res==1:
            break
        l=i+1
        r=n-1
        while l < r:
            if arr[i]+arr[l]+arr[r] == sum:
                res=1
                break
            elif arr[i]+arr[l]+arr[r] < sum:
                l=l+1
            else:
                r=r-1
    print res
    t=t-1
