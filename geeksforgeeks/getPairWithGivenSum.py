"""
Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.
Input  :  arr[] = {1, 5, 7, -1},
          sum = 6
Output : (1, 5) (7, -1)
"""
def search_array(first_val, arr, first_index, last_index, sum_to_find):
    # print(arr, first_index, last_index, sum_to_find)
    if last_index >= first_index:

        mid = int(first_index + (last_index - first_index) / 2)
        # print('mid: ',mid)
        # print('arr[mid]: ',arr[mid])
        # print('first_val: ', first_val)

        # Found the pair, return them
        if arr[mid] + first_val == sum_to_find:
            return (arr[mid],first_val)

        # search in lower half of array
        elif arr[mid] + first_val > sum_to_find:
            return search_array(first_val, arr, first_index, mid - 1, sum_to_find)

        # search in upper half of array
        elif arr[mid] + first_val < sum_to_find:
            return search_array(first_val, arr, mid + 1, last_index, sum_to_find)

    # Not found the pair in the array, return -1
    else:
        return -1

# Get all inputs
arr = [int(x) for x in input('Enter a list of integers (separated by space)').split()]
sum_to_find = int(input('Enter a integer (sum of pairs to be find)'))
# arr = [-10,-2,0, -2, -3, -4, -7,-9,14,17]
# sum_to_find = -7

# Sort the array
arr.sort()

# Iterate over all element and try searching for other element in the remaining array
for i in range(len(arr)-1):
    result = search_array(arr[i], arr, i + 1, len(arr) - 1, sum_to_find)
    if result != -1: print(result)

'''
arr.sort()

-5,-1,1,2,3,6,8,10

-1, 10 total_sum < sum_to_find 
+ total_sum > sum_to_find 

-5 10 --> 5 < sum_to_find 

indexes of array
0,1,2,3,4,5,6,7,8,9,10

1,2,3,4   ,5,    6,7,8,9,10
0 + 5 < sum_to_find ---> 0 + 8
0 + 5 > sum_to_find ---> 0 + 2


-1 10 --> 9

---------------------
max + min < sum_to_find


max + min > sum_to_find

2nd_max + min
3rd_max + min

---------------------
10, 2
10, 1
10, 3

2,1
2,3

1,3
'''