class Solution:

  #Sliding interval optimized method
	def removals(self,arr, n, k):
		# code here
		i=0
		j=0
		maxi=0
		arr.sort()
		while(j<n):
		    if arr[j]-arr[i]<=k:
		        maxi = max(maxi,j-i+1)
		        j+=1
		    elif i<j:
		        i+=1
		    #print(j,i)
		
		return n-maxi
