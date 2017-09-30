"""
Given a decimal number m. Convert it in binary string and apply n iterations, in each iteration 0 becomes 01 and 1 becomes 10. Find kth character in the string after nth iteration.

Input:
The first line consists of an integer T i.e number of test cases. The first and only line of each test case consists of three integers m,k,n. 

Output:
Print the required output.

Constraints: 
1<=T<=100
1<=m<=50
1<=n<=10
0<=k<=|Length of final string|

Example:
Input:
2
5 5 3
11 6 4

Output:
1
1
"""

for t in range(int(input())):
    m,k,n = [int(x) for x in input().split()]
    m = bin(m)[2:]
    for c in range(n):
        new = ""
        for i in m:
            if i == "1":
                new += "10"
            else:
                new += "01"
        m = new
    try: print(m[k])
    except IndexError: print("")