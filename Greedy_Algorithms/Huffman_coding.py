class Node:
    def __init__(self,symbol,freq,left=None,right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right
        self.huff = ''

def printNodes(node,val=''):
    newval = val+str(node.huff)

    #if node is not an edge node, then traverse inside
    if(node.left):
        printNodes(node.left,newval)

    if(node.right):
        printNodes(node.right,newval)

    #If node is edge node, display it's huffman code
    if(not node.left and not node.right):
        print(f"{node.symbol}->{newval}")

chars = ['a','b','c','d','e','f']

freq = [ 5, 9, 12, 13, 16, 45]

#list containing unused nodes
nodes=[]

for i in range(len(chars)):
    nodes.append(Node(chars[i],freq[i]))

while len(nodes)>1:
    #Sort every time
    nodes = sorted(nodes,key=lambda x:x.freq)
    #pick smallest 2 nodes
    left = nodes[0]
    right = nodes[1]

    #assign directional values to these nodes.
    left.huff = 0
    right.huff = 1

    #create newnode by adding freq
    newnode = Node(left.symbol+right.symbol,left.freq+right.freq,left,right)

    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newnode)

#Print huffman tree
printNodes(nodes[0])

# Output:
# f->0
# c->100
# d->101
# a->1100
# b->1101
# e->111
