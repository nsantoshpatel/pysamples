""" 
Given an string in roman no format (s)  your task is to convert it to integer .

Input:
The first line of each test case contains the no of test cases T. Then T test cases follow. Each test case contains a string s denoting the roman no.

Output:
For each test case in a new line print the integer representation of roman number s. 

Example:
Input
2
V
III 
Output
5
3
"""
count = raw_input()
mapList = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
try:
    for x in range(int(count)):
        roman = raw_input(); sum = 0
        for x,item in enumerate(roman[:-1]):
            if mapList.get(item,0) >= mapList.get(roman[x+1],0):
                sum += mapList.get(item,0)
                #print sum, mapList.get(item,0), "+"
            else:
                sum -= mapList.get(item,0)
                #print sum, mapList.get(item,0), "-"
        sum += mapList.get(roman[-1],0)
        print sum

except ValueError:
    print "ERROR: incorrect Integer input"
