def countsetbits(b):
    count=0
    while(b>0):
        count=count+(b&1)
        b=b>>1
    return count

t = int(raw_input())
while t>0:
    a=map(int,raw_input().split())
    b=a[0]^a[1]
    print countsetbits(b)
    t=t-1
