#User function Template for python3

#Instead of going 0->N, go N->0 without the need of recursion/dp.
class Solution:
    def minOperation(self, n):
        # code here 
        count=0
        while n>0:
            if n%2==0:
                n=n/2
            else:
                n=n-1
            count+=1
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends
