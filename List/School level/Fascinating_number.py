class Solution:

	def fascinating(self,n):
	    # code here
	    a=str(n*2)
	    b=str(n*3)
	    s=str(n)+a+b
	    mylist = [int(i) for i in s]
	    #print(mylist)
	    for i in range(1,10):
	        #print(i)
	        if i not in mylist:
	            return False
	        else:
	            mylist.remove(i)
	    if len(mylist)==0:
	        return True
