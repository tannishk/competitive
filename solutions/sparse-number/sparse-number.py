n = int(raw_input())
while(n>0):
    a = int(raw_input())
    j = a>>1
    if(a & j):
        print '0'
    else:
        print '1'
    n=n-1
