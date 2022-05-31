#Flattening of a linked list (Nice question)
#dummy node -  2 pointers (res and temp)
#flatten last 2 lists, and then continue to do that recursively.
#merge 2 at a time.

def flatten(root):
    #Your code here
    if(root==None or root.next==None):
        return root
    
    #recursive call
    root.next = flatten(root.next)
    
    #merge
    root = mergeTwoLists(root,root.next)
    
    return root
    
def mergeTwoLists(a,b):
    temp = Node(0)
    res=temp
    
    while(a!=None and b!=None):
        if(a.data<b.data):
            temp.bottom = a
            a = a.bottom
            temp=temp.bottom
        else:
            temp.bottom = b
            temp = temp.bottom
            b = b.bottom
    
    temp.bottom = a if(a!=None) else b
    return res.bottom
