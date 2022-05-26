from collections import defaultdict
class Graph:
    ##constructor
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,start):

        #Mark all vertices as not visited.
        visited = [False] * (max(self.graph) + 1)

        #Create a queue for BFS
        queue = []

        #Mark start node as visited and enqueue it.
        queue.append(start)
        visited[start] = True

        while queue:
            #Dequeue a vertex from queue and print it.
            s = queue.pop()
            print(s, end=" ")

            #Get all adjacent vertices of the dequeued  vertex s. If not visited, mark as visited and enqueue it.
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
    
    def DFS(self,start):

        #Mark all vertices as not visited.
        dfs_visited = [False] * (max(self.graph)+1)

        self.dfs_traversal(start,dfs_visited)

    def dfs_traversal(self,s,dfs_visited):

        #Base case
        if dfs_visited[s]==True:
            return
        else:
            dfs_visited[s]=True
            print(s, end= " ")

        for i in self.graph[s]:
            self.dfs_traversal(i,dfs_visited)
        

def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("BFS Starting from vertex/node 2: ")
    g.BFS(2)
    print("\n")
    g.DFS(2)

if __name__ == "__main__":
    main()

# Output
# BFS Starting from vertex/node 2: 
# 2 3 0 1

# 2 0 1 3
