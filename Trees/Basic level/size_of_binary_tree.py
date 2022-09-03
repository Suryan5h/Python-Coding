def getSize(node):
    # code here
    if node==None:
        return 0
    
    return getSize(node.left)+1+getSize(node.right)
