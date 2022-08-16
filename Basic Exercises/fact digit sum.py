class Solution:
	def FactDigit(self, N):
		# Code here
		fact=[0]*10
		fact[0]=1
        for i in range(1,10):
            fact[i] = i*fact[i-1]
        
        ans=list()
        for i in range(9,0,-1):
            while(N>=fact[i]):
                N-=fact[i]
                ans.append(i)
        
        return ans[::-1]
