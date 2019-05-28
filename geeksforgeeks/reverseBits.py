'''
Given a 32 bit number x, reverse its binary form and print the answer in decimal.

Input:
The first line of input consists T denoting the number of test cases. T testcases follow. Each test case contains a single 32 bit integer

Output:
For each test case, in a new line, print the reverse of integer.

Constraints:
1 <= T <= 100
0 <= x <= 4294967295

Example:
Input:
2
1
5
Output:
2147483648
2684354560

Explanation:
Testcase1:
00000000000000000000000000000001 =1
10000000000000000000000000000000 =2147483648
'''

for i in range(int(input())):
    binary_str = bin(int(input())).replace("0b","")
    print(int(("0" * (32 - len(binary_str)) + binary_str)[::-1],2))
