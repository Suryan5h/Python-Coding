class Node:

    def __init__(self,data):
        #Assign data
        self.data = data
        #Assign next to None
        self.next = None

class LinkedList:

    #Function to initialize head
    def __init__(self):
        self.head = None

    #Insert the node at the beginning
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        node=self.head
        while node:
            print(str(node.data)+"->",end="")
            node = node.next
        print("NULL") 

    def findMiddle(self):
        #Initialize 2 pointers slow and fast
        #Slow moves 1 step at a time
        #fast moves 2 step at a time
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print("Middle Element is: ",slow.data)


def main():

    #Initialize head/linked list
    mylist = LinkedList()

    #Add elements 6,5,4,3,2,1 and insert the nodes at the beginning
    for i in range(6,0,-1):
        mylist.push(i)
    
    #Print linkedlist
    mylist.printlist()

    #Find middle of linked list using 2 pointers
    mylist.findMiddle()

if __name__ == "__main__":
    main()
    
 
# 1->2->3->4->5->6->NULL
# Middle Element is:  4
