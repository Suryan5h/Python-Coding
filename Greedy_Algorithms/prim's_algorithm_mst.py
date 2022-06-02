#User function Template for python3
#Note :  Very good usage of heapq. (priority queue).
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        key=[float('inf')]*(V)
        
        visited=[False]*(V)
        
        par=[-1]*(V)
        
        key[0]=0
        par[0]=-1
        l=[]
        heapq.heappush(l,(0,0))
        while l:
            di,curr=heapq.heappop(l)
            visited[curr]=True
            for i in adj[curr]:
                node=i[0]
                d=i[1]
                if not visited[node] and d<key[node]:
                    par[node]=curr
                    key[node]=d
                    heapq.heappush(l,(key[node],node))
                    
        return sum(key)  
        
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
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends
