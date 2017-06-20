astr = "madam"
alen= len(astr)

print astr == astr[::-1]
for x in range(alen/2):
    if not astr[x] == astr[alen-1-x]:
        print False 
        break
else:
    print True
