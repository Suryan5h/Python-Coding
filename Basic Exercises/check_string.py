class Solution:
    def check (self,s):
        # your code here
        first=s[0]
        for i in range(1,len(s)):
            if first!=s[i]:
                return False
        return True
