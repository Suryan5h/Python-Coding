def getNth(head, k):
    # Code here
    temp=head
    count=0
    while(temp!=None):
        count+=1
        if k==count:
            return temp.data
        else:
            temp = temp.next
