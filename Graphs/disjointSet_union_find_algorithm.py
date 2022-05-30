#User function Template for python3


class Solution:
    
    #Function to merge two nodes a and b.
    def findPar(self,x,par):
        if x == par[x]:
            return x
        
        par[x] = self.findPar(par[x],par)
        return par[x]
        
    def union_(self,a,b,par,rank1):
        # code here
        u = self.findPar(a,par)
        v = self.findPar(b,par)
        
        if rank1[u]<rank1[v]:
            par[u]=v
        elif rank1[v]<rank1[u]:
            par[v]=u
        else:
            par[v]=u
            rank1[u] += 1
        
    #Function to check whether 2 nodes are connected or not.
    def isConnected(self,x,y,par,rank1):
        # code here
        x = self.findPar(x,par)
        y = self.findPar(y,par)
        
        if x == y:
            return 1
        else:
            return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        q = int(input())

        par = [i for i in range(n+1)] # parent of ith node is initialized as i.
        rank1 = [1 for i in range(n+1)] # rank is initialized as 1 fo every node
        obj = Solution()
        for i in range(q):
            task,u,v = map(str,input().strip().split())
            u = int(u)
            v = int(v)

            if task == 'U':
                obj.union_(u,v,par,rank1)
            else:
                if obj.isConnected(u,v,par,rank1):
                    print(1)
                else:
                    print(0)


# } Driver Code Ends

# Input:
# N = 5
# q = 4
# Queries = 
# Union(1,3)
# isConnected(1,2)
# Union(1,5)
# isConnected(3,5)

# Output:
# 0
# 1
# Explanation: Initially all nodes 1 2 3 4 5
# are not connected. 
# After Union(1,3), node 1 and 3 will be
# connected.
# When we do isConnected(1,2),  as node 1
# and 2 are not connected it will return 0.
# After Union(1,5), node 1 and 5 will be
# connected.
# When we do isConnected(3,5),  as node
# 1 and 3 are connected, and node 1 and 5
# are connected, hence 3 and 5 are
# connected. Thus it will return 1.


