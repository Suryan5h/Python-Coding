#User function Template for python3

class Solution:
    def transitiveClosure(self, N, graph):
        # code here
        #Create "ans" 2d list[list] to store our answer.
        ans = [[0 for x in range(N)] for y in range(N)]
        #create adjacency list from given graph.
        #If value in graph == 1, we can add in adjacency list.
        adj=[[] for x in range(N)]
        for i in range(N):
            for j in range(N):
                if graph[i][j]==1:
                    adj[i].append(j)
        #print(adj)
        
        #Since, diagonal is always reachable, it means 0 is reachable by 0
        #1 is always reachable by 1
        #So we put diagonals as 1.
        #ans[v][v]=1
        #we all DFS function passing adj list, ans, root, adjacent/descendant.
        
        #This is DFS call for each vertex inside for loop.
        for v in range(N):
            ans[v][v]=1
            self.DFS(adj,ans,v,v)
        
        return ans
    
    def DFS(self,adj,ans,root,descendant):
        
        #Check for each child of the adjacent.
        #it means, suppose we passed 1,1 for 1st row, it will check all the adjacents of 1. (1 and 2).
        #for each child of adjacent , (1 and 2),
        #we check if ans is 0, it means not visited.
        #So we check for 2.
        #Then we check 2 as reachable from root (0) and call DFS function to find that 3 is also reachable by 0.
        #Since 3 is a adjacent of 2.
        for child in adj[descendant]:
            if ans[root][child]==0:
                ans[root][child]=1
                self.DFS(adj,ans,root,child)
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        graph = []
        for i in range(0,N):
            graph.append([int(j) for j in input().split()])
        ob = Solution()
        ans = ob.transitiveClosure(N, graph)
        for i in range(N):
            for j in range(N):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends
