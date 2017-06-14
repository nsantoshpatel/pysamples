"""
Write a program to Print for n=3,5,7,...... 
if n=3 print 
* 
** 
*, 
For n=5,print, 
* 
** 
***
** 
*....so on.....only for odd numbers.
"""
import sys
try:
    n = int(raw_input())
except ValueError:
    sys.exit("ERROR: integer value expected")
if not n%2==1: sys.exit("ERROR: Odd Number expected")

list1 = ["*"*(i+1) if i <= n/2 else "*"*(n-i) for i in range(n)]
for j in list1: print j

#~ for i in range(n):
    #~ if i <= n/2:
        #~ print "*"*(i+1)
    #~ else:
        #~ print "*"*(n-i)
