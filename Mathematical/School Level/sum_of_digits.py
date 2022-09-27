class Solution:
    def sumOfDigits (self, N):
        # code here
        temp=N
        sumi=0
        while(temp>0):
            digit = temp%10
            sumi+=digit
            temp=temp//10
        return sumi
