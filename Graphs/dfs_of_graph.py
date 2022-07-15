##Simple solution
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        def dfs(i,vis,adj,storedfs):
            vis[i]=True
            storedfs.append(i)
            
            for k in adj[i]:
                if vis[k]==False:
                    dfs(k,vis,adj,storedfs)
            
            
        vis=[False] * (V)
        storedfs=[]
        for i in range(V):
            if vis[i]==False:
                dfs(i,vis,adj,storedfs)
        return storedfs
