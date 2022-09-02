def isLengthEvenOrOdd(head):
    # Code here
    temp=head
    size=0
    while(temp!=None):
        size+=1
        temp=temp.next
    if size%2==0:
        return False
    else:
        return True
