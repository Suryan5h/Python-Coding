def countWays(self,n):
        
        # code here
        mod = 1e9+7
        dp = [-1]*(n+1)
        def f(n):
            if n<=1:
                return 1
            
            if dp[n]!=-1:
                return dp[n]%mod
            else:
                dp[n]=f(n-1)+f(n-2)
                return dp[n]%mod
        ans = f(n)
        return int(ans)
      
  ## Basically, another problem of fibonacci problem. Just different words.
