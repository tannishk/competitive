'''
Print a sequence of numbers starting with N, without using loop, in which A[i+1] = A[i] - 5, if A[i]>0, else A[i+1]=A[i] + 5 repeat it until A[i]=N.

Input:
First line contains number of test cases T. Then following T lines contains an integer N.

Output:
Single line with pattern .

Constraints:
0< N < 10000

Example:
Input:
2
16
10

Output: 
16 11 6 1 -4 1 6 11 16
10 5 0 5 10

Explanation:
We basically first reduce 5 one by one until we reach a negative or 0. After we reach 0 or negative, we one by one add 5 until we reach N.
'''

import sys

info = sys.argv

def recurs(num, ognum, passed_middle):
	if num > ognum:
		print ''
		return
	elif num > 0 and not passed_middle:
		sys.stdout.write('%d  ' % num)
		if (num - 5) <= 0:
			passed_middle = True
		recurs(num - 5, ognum, passed_middle)
	else:
		sys.stdout.write('%d  ' % num)
		recurs(num + 5, ognum, passed_middle)

for num in info[2:]:
	recurs(int(num), int(num), False)

