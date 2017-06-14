'''Given a positive integer n, find if it can be expressed as x^y where y > 1 and x > 0 and x and y both are both integers.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow . Each test cases contains an integer N.

Output:
For each test case in a new line print 1 if the number can be expressed as  xy else print 0.

Constraints:
1<=T<=1000
1<=n<=100

Example:
Input:
2
8
5
Output:
1
0
'''
from math import sqrt
def tmpFunc(A):
    if A==1: return 1
    for x in range(int(sqrt(A)),1,-1): 
        tmp = x
        for y in range(2,6):
            print("x:"+str(x)+" y:"+str(y))
            tmp = tmp*x
            print("tmp:"+str(tmp))
            if tmp == A: return 1
            if tmp > A: break
    else:
        return 0
for ic in range(int(input())):
    print(tmpFunc(int(input())))
