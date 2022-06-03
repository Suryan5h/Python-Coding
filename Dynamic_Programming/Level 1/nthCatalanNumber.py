#User function Template for python3

class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        #return the nth Catalan number.
        #base case
        if n<=1:
            return 1
          
        #c3=c0.c3 + c1.c2 + c2.c1 + c3.c0
        dp = [0 for i in range(n+1)]
        dp[0]=1
        dp[1]=1
        
        for i in range(2,n+1):
            dp[i]=0
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        
        return dp[n]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        
        print(Solution().findCatalan(n))
        
# } Driver Code Ends
