class Solution:
	def is_palindrome(self, n):
		# Code here
		n=str(n)
		rev = n[::-1]
		if rev==n:
		    return "Yes"
		else:
		    return "No"
