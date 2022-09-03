# function should return the count of total number of non leaf nodes in the tree
class Solution:
    def countNonLeafNodes(self, root):
        # add code here
        if root==None:
            return 0
        
        if root.left==None and root.right==None:
            return 0
        
        return 1+self.countNonLeafNodes(root.left)+self.countNonLeafNodes(root.right)
