'''
Given an alphanumeric string return string with only digit positions reversed

Input "12 3.4%5?"
Output "54 3.2%1?"
'''

def rev_str(a):
    y = [x for x in a[::-1] if x.isdigit()]
    res = ""
    cnt = 0
    for i in a:
        if i.isdigit():
            res+=y[cnt]
            cnt += 1
        else:
            res+=i
    return res

print(rev_str('123fsdi45'))