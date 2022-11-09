class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self,s):
        #code here
        import re
        result=0
        pattern = r'[0-9]*'
        ans = re.findall(pattern,s)
        for item in ans:
            if item!='':
                result+=int(item)
                #print(item)
        return result
      
 # Using Regex.
