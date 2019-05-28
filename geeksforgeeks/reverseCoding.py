"""
Sherlock Being tired with the usual coding rounds started growing his interest towards reverse coding when he won the event in his college symposium. He wondered if his friend has the brain to quickly identify the pattern and verify if his inputs are correct or not. From the example portion given below, where you will be given a number(n) and its output, Using this find the pattern. Your task is that from the pattern you identified above, You have to tell if for the given n whether the given m is the correct answer or not...

Input:
The first line consists of T, the number of test cases. then T lines follow. Each line consists of n and m.

Output:
For each n and m output 1 if m is the corresponsing input for the value of n and 0 otherwise.

Constraints:
1<=t<=50
0<=n<=1000
0<=m<=10^6

Example to identify the pattern :

Input                            Output

10                                 55

20                                 210

5                                   15

0                                    0

1                                    1

2                                    3

Example:
Input:
4
10 55
4 11
2  3
6 21

Output:
1
0
1
1
"""
def getOutput(num):
    if num%2:
        ret = num * (num/2 + 0.5)
    else:
        ret = num * (num/2) + (num/2)
    return int(ret)

for i in range(int(input())):
    num, ext = [int(x) for x in input().split()]
    if ext == getOutput(num):
        print(1)
    else:
        print(0)
