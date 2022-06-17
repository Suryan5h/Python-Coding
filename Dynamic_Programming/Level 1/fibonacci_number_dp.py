def f(n):
    if n<=1:
        return n
    
    if dp[n]!=-10:
        return dp[n]
    else: 
        dp[n] = f(n-1)+f(n-2)
        return dp[n]

n=int(input())
dp = [-10]*(n+1)
print(f(n))
