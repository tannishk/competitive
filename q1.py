'''Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that have exactly k distinct characters.

Input:

The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two lines. The first line of each test case consists of a string S.
The second line of each test case contains integer K.

Output:

Corresponding to each test case, in a new line, print the count all possible substrings that has exactly k distinct characters.

Constraints:

1 ≤ T ≤ 100
1 ≤ string length ≤ 1000
1 ≤ K ≤ 26

Example:

Input
2
aba
2

Output
3

'''
#code
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
