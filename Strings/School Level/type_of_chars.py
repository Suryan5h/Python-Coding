class Solution:
    def count (self,s):
        # your code here
        ans = [0]*4
        for i in s:
            if i.isupper():
                ans[0]+=1
            elif i.islower():
                ans[1]+=1
            elif i.isnumeric():
                ans[2]+=1
            else:
                ans[3]+=1
        return ans
