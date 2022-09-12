class Solution:
    def distinctCount(self, arr, n):
        # code here
        a=set()
        for i in arr:
            if abs(i) not in a:
                a.add(abs(i))
        return len(a)
