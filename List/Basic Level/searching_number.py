# Searching number's first occurence in an array
class Solution:
	def search(self,arr, n, k): 
    	# code here
    	for i in range(n):
    	    if arr[i]==k:
    	        return i+1
    	return -1
