class Solution:

    def extractIntegerWords(self, s):
        # code here
        import re
        pattern = r'[0-9]+'
        ans = re.findall(pattern,s)
        return ans
