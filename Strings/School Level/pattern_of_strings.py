class Solution:
	def pattern(self, S):
		# code here
		ans=[]
		for i in range(len(S)):
		    ans.append(S[:len(S)-i])
		return ans
