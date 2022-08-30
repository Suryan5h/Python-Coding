class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        rev = arr[::-1]
        # print(rev)
        # print(arr)
        if rev==arr:
            return True
        else:
            return False
