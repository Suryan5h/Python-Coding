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

if __name__ == "__main__":
    main()
    
# Output:    
# BFS Starting from vertex/node 2: 
# 2 3 0 1
