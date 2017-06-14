"""
Given an array A of size N, find all combination of four elements in the array whose sum is equal to a given value K.. For example, if the given array is {10, 2, 3, 4, 5, 9, 7, 8} and K = 23, one of the quadruple is "3 5 7 8"
Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of input contains two integers N and K. Then in the next line are N space separated values of the array.
Output:
For each test case in a new line print all the quadruples present in the array separated by space which sums up to value of K. Each quadruple is unique which are separated by a delimeter "$" and are in increasing order.
Example:
Input:
2
5 3
0 0 2 1 1 
7 23
10 2 3 4 5 7 8
Output:
0 0 1 2 $
2 3 8 10 $2 4 7 10 $3 5 7 8 $
"""
count = int(input())
for x in range(count):
    len1, sum1 = tuple(int(x) for x in input().split())
    list1 = sorted(list(int(x) for x in input().split()))
    print(list1)
    result = ""
    for a in range(len1):
        suma = list1[a]
        if suma > sum1: break
        for b in range(a+1,len1):
            sumb = suma+list1[b]
            if sumb > sum1: break
            for c in range(b+1, len1):
                sumc = sumb+list1[c]
                if sumc > sum1: break
                for d in range(c+1, len1):
                    sumd = sumc+list1[d]
                    if sumd == sum1:
                        addStr = " ".join(map(str,sorted([list1[a],list1[b],list1[c],list1[d]])))
                        if not addStr in result: 
                            result += addStr + " $"
                    elif sumd > sum1: break
    print(result)

#~ list1 = [10,10,20,30,40,50,60,80]
#~ len1 = len(list1)
#~ sum1 = 200
