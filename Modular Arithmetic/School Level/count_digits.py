class Solution:
    def evenlyDivides (self, N):
        # code here
        temp=N
        count=0
        while(temp>0):
            dig = temp%10
            temp = temp//10
            if dig!=0:
                if N%dig == 0:
                    count+=1
        return count
