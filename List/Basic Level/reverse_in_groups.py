class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code here
		i=0
		ans=[]
		while(K+i<=len(arr)):
		    temp=arr[i:K+i]
		    temp = temp[::-1]
		    arr[i:K+i] = temp
		    i=i+K
	    temp=arr[i:]
	    temp=temp[::-1]
	    arr[i:] = temp
