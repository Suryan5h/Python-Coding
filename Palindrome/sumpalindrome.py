class Solution:
    def isSumPalindrome (self, n):
        # code here
        i=0
        temp = n
        while(i<6):
            if str(temp)==(str(temp)[::-1]):
                return temp
            temp += int(str(temp)[::-1])
            #print(temp)
            i+=1
        return -1
