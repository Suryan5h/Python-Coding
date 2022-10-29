# Goldman Sachs

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        if len(A)!=len(B):
            return False
            
        #code here
        A = sorted(A)
        B = sorted(B)
        for i in range(len(A)):
            if A[i]!=B[i]:
                return False
        return True
