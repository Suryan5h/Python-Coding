class Solution:
    def isDigitSumPalindrome(self,N):
        #code here
        temp=N
        sumi=0
        while(temp>0):
            dig=temp%10
            temp=temp//10
            sumi+=dig
        rev = int(str(sumi)[::-1])
        if rev==sumi:
            return 1
        else:
            return 0
