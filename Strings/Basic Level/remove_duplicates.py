class Solution:
	def removeDups(self, S):
		# code here
		a=[]
		for i in S:
		    if i not in a:
		        a.append(i)
		ans = ''.join(a)
		return ans
