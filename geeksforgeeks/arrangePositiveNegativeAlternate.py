"""
Given an array containing equal number of positive and negative elements, arrange the array such that every positive element is followed by a negative element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, in a new line print the arranged array.

Constraints:
1<=T<=300
2<=N<=105
-105<=A[i]<=105

Example:
Input:
2
6
-1 2 -3 4 -5 6
4
-3 2 -4 1
Output:
2 -1 4 -3 6 -5
2 -3 1 -4
"""
#code
for iters in range(int(input())):    
    n = int(input())
    a = [int(z) for z in input().split()]
    new_a = ""
    for i in range(0, n, 2):
        for x in a:
            if x>0:
                new_a = new_a + str(x) + " "
                a.remove(x)
                break
        for x in a:
            if x<0:
                new_a = new_a + str(x) + " "
                a.remove(x)
                break

    print(new_a)