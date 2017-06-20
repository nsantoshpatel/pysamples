astr = 'helloolleh'
adict = {}

for x in astr:
    if x in adict.keys():
        adict[x] += 1
    else: 
        adict[x] = 1

#~ afilter = filter((lambda x: x % 2 ==0 ), adict.values())
afilter = [y for y in adict.values() if not y%2]
if len(afilter) == len(adict.keys()) or len(afilter)+1 == len(adict.keys()) :
    print True
    
else:
    print False
