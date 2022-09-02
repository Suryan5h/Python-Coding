def areIdentical(head1, head2):
    # Code here
    temp1=head1
    temp2=head2
    while(temp1!=None and temp2!=None):
        if temp1.data != temp2.data:
            return False
        else:
            temp1 = temp1.next
            temp2 = temp2.next
    return True
