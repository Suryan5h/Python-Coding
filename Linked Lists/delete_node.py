#Delete Node in a linked list
#Just shift the right side of the node and replace the value. In a way it deletes the value from list.
#Dumb solution and question.
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #Edge case
        if(node.next==None):
            node=None
        node.val = node.next.val
        node.next = node.next.next
