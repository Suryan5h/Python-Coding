class Solution:

	def getMoreAndLess(self,arr, n, x):
		# code here
        ans=[None]*2
        ans[0]=0
        ans[1]=0
        for i in arr:
            if i<=x:
                ans[0]+=1
            if i>=x:
                ans[1]+=1
        return ans
