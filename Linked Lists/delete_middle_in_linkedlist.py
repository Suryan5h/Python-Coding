#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    
    #code here
    #Find middle element first
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    #print("Middle Element is: ",slow.data)
    
    temp=head
    while temp.next != slow:
        temp = temp.next
    
    temp.next = slow.next
    return head

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n=int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)

        res=deleteMid(ll.head)
        printList(res)
# } Driver Code Ends
