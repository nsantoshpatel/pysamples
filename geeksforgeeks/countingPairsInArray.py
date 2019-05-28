def func(arr, length):
    ret = 0
    for i in range(length-1):
        for j in range(i+1,length):
            if i * arr[i] > j * arr[j]:
                # print(arr[i], arr[j])
                ret += 1
    return ret
for x in range(int(input())):
    length = int(input())
    arr = [int(i) for i in input().split()]
    print(func(arr, length))

