"""
Given a 2D array, find the maximum sum subarray in it. For example, in the following 2D array, the maximum sum subarray is highlighted with blue rectangle and sum of this subarray is 29.

Array
-----
 1  2 -1 -4 -20 
-8 -3  4  2  1 
 3  8 10  1  3 
-4 -1  1  7 -6

Input:
First line of every test case consists of T test case. First line of every test case consists of 2 integers R and C , denoting number of rows and columns. Second line consists of R*C spaced integers denoting number of elements in array.

Output:
Single line output, print the Max sum forming a rectangle in a 2-D matrix

Example:
Input:
1
4 5
1 2 -1 -4 -20 -8 -3 4 2 1 3 8 10 1 3 -4 -1 1 7 -6
Ouptut:
29
Explanatin:
Subarray with max sum
--------
-3  4  2 
 8 10  1 
-1  1  7 
"""

for count in range(int(input())):
    r,c = (int(x) for x in input().split())
    arr = input().split()
    msum = int(arr[0])
    
    for row in range(r):
        for col in range(c):
            
            for row1 in range(row,r):
                for col1 in range(col,c):
                    
                    tsum = 0
                    for row2 in range(row,row1+1):
                        for col2 in range(col,col1+1):
                            tsum += int(arr[row2*c+col2])
                        if tsum > msum: msum = tsum
                        
    print(msum)