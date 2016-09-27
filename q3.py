Sum Of Digits
Given an integer N, find sum of all digits of N.

Input:

The first line contains an integer T, total number of test cases. Then following T lines contains an integer N.

Output:

Calculate the sum of digits of N.

Constraints:

1 ≤ T ≤ 30

1 ≤ N ≤ 1000

Example:

Input
2
123
45

Output
6
9

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
