"""
Given an array. The task is to arrange the array such that odd elements occupy the odd positions and even elements occupy the even positions. The order of elements must remain same. Consider zero-based indexing. After printing according to conditions, if remaining, print the remaining elements as it is.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.
Output:
For each test case, in a new line print the arranged array.

Constraints:
1<=T<=100
1<=N<=105
1<=A[i]<=105

Example:
Input:
2
6
1 2 3 4 5 6
4
3 2 4 1
Output:
2 1 4 3 6 5
2 3 4 1
"""

# for i_count in range(int(input())):
#     size = int(input())
array = list(int(x) for x in input().split())
evenPos = 0
result = []
size = len(array)

odd_list = []
even_list = []

for i in array:
    if i%2:
        odd_list.append(i)
    else:
        even_list.append(i)



for i in range(size):
    if evenPos:
        for j in array:
            if j%2:
                result.append(j)
                array.remove(j)
                break
        evenPos = 0
    else:
        for j in array:
            if not j%2:
                result.append(j)
                array.remove(j)
                break
        evenPos = 1
else:
    result.extend(array)
print(result)




