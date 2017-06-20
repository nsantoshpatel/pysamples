from random import randint
alist = [randint(0,100) for i in range(10)]
alen = len(alist)
print alist
sort = 'bubble'
#~ sort = 'insert'

# ===================
# Bubble Sorting : [4]
''' Looping Count:
= (n-1)+(n-2)+(n-3)....(n-n) 
= n*n - n(n+1)/2
= n*n/2 - n/2
= n(n-1)/2
'''
if 'bubble' in sort:
    for x in xrange(alen-1):
        for y in xrange(x,alen-1):
            if alist[y] > alist[y+1]:
                alist[y+1], alist[y] = alist[y], alist[y+1]

# ===================
# Insertion Sorting
''' Looping Count = 0+1+2+3....(n-1)  [MAXIMUM]
= (n-1)(n)/2'''
if 'insert' in sort:
    for x in xrange(alen):
        for y in xrange(x):
            if alist[x] < alist[y]:
                # alist[x], alist[y] = alist[y], alist[x]
                t = alist.pop(x)
                alist.insert(y, t)
                break

print alist
