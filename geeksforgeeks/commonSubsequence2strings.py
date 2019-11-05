""" 
Given two strings a and b print whether they contain any common subsequence (non empty) or not.

Input:
The first line contains an integer T denoting number of testcases. Each of the next T lines contains two strings a and b.

Output:
Print 1 if they have a common subsequence (non empty) else 0.

Constraints:
1<=T<=10^5
1<= |a|=|b| <=30
a and b consist of uppercase English letters ('A'....'Z')

Example:
Input:
1
ABEF CADE
Output:
1

Explanation:
AE is a subsequence of both the string so the answer is 1
"""

for count in range(int(input())):
    a, b = input().split()
    for x in a:
        if x in b: 
            print(1)
            break
    else:
        print(0)

"""
def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer
"""