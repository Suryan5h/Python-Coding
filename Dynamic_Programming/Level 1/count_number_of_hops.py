#geeksforgeeks

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        
        mod = 1e9+7
        dp = [-1]*(n+1)
        # code here
        def f(n):
            if n<=1:
                return 1
            
            if n==2:
                return 2
            
            if n==3:
                return 4
            
            if dp[n]!=-1:
                return dp[n]%mod
                
            one = f(n-1)
            two = f(n-2)
            three = f(n-3)
            dp[n] = one+two+three
            return dp[n]%mod
            
        ans = f(n)
        return int(ans)
