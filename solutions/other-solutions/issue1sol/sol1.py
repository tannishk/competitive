import sys
change = 0
def pri(n,change,var):
    if change == 1 and var==n:
        sys.stdout.write(str(n))
        sys.stdout.write(' ')
        return;
    if change==0 and n>0:
        sys.stdout.write(str(n))
        sys.stdout.write(' ')
        pri(n-5,0,var)
    elif change==0 and n<=0:
        sys.stdout.write(str(n))
        sys.stdout.write(' ')
        #change = 1
        pri(n+5,1,var)
    elif change==1 and n>0:
        sys.stdout.write(str(n))
        sys.stdout.write(' ')
        pri(n+5,1,var)
    
t = int(raw_input())
while t>0:
    n = int(raw_input())
    var = n
    change=0
    pri(n,0,n)
    print ''
    t=t-1
