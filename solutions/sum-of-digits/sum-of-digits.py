def toto(a):
    if(a==0):
        return 0
    else:
        return (a%10)+toto(a/10)

t = int(raw_input())
while(t>0):
    n=int(raw_input())
    print toto(int(n))
    t=t-1
