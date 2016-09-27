You are given two numbers A and B. Write a program to count number of bits needed to be flipped to convert A to B.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is a and b.

Output:

Print the number of bits needed to be flipped.

Constraints:

1 ≤ T ≤ 100
1 ≤ a,b ≤ 1000

Example:

Example:
Input
1
10 20

Output
4
 

Explanation:

A  = 1001001
B  = 0010101
No of bits need to flipped = set bit count i.e. 4


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
