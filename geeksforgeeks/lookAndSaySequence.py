"""
Given a pattern as below and an integer n your task is to decode it and print nth row of it. The pattern follows as :
1
11
21
1211
111221
............

Input:
The first line of input is the number of test cases .  Then T test cases follow . The first line of each test case is an integer N.

Output:
For each test case print the required nth row of the pattern.

Constraints:
1<=T<=20
1<=N<=20

Example:
Input:
2
2
3
Output:
11
21
"""
for t in range(int(input())):
    pattern = "1"
    for i in range(int(input())-1):
        prev = ""
        times = 0
        res = ""
        for nex in pattern:
            if not nex == prev:
                if not prev == "": res += str(times)+ prev
                prev = nex
                times = 1
            else:
                times += 1
        else:
            res += str(times)+ prev
        pattern = res
    print(pattern)
    
