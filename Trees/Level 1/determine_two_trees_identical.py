class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here
        if root1 is None and root2 is None:
            return True
        
        return (root1 is not None and root2 is not None) and (root1.data==root2.data) and self.isIdentical(root1.left,root2.left) and self.isIdentical(root1.right,root2.right)
