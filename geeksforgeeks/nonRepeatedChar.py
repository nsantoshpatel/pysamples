"""
Given a string s consisting of lowercase Latin Letters, find the first non repeating character in s.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases.
Each case begins with a single integer N denoting the length of string. The next line contains the string s.
 
Output:
For each testcase, print the first non repeating character present in string.
Print -1 if there is no non repeating character

Example:
Input :
3
5  
hello
12
zxvczbtxyzvy
6
xxyyzz

Output :
h
c
-1
"""
#~ count = int(input());
count = int(raw_input());
for i in range(count):
    #~ letterCount = int(input());
    letterCount = int(raw_input());
    #~ word = input();
    word = raw_input();
    l = [];
    #~ for i in word:
        #~ if not i in l:
            #~ if word.count(i) == 1: 
                #~ print(i);
                #~ break;
            #~ else: 
                #~ l.append(i);
    #~ else:
        #~ print("-1");

    for x in range(letterCount):
        if word[x] not in l:
            for i_word in word[x+1:]:
                if word[x] == i_word:
                    l.append(word[x])
                    break
            else:
                print(word[x])
                break
    else:
        print("-1")
