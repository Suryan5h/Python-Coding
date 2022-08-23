class Solution:
    def leftElement(self, arr, n):
        # Your code goes here
        arr = sorted(arr)
        if n%2==0:
            return arr[(n//2)-1]
        else:
            return arr[n//2]
