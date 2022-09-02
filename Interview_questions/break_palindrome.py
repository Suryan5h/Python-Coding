def checkpalin(temp):
    t = temp[::-1]
    if t==temp:
        return True
    else:
        return False

def breakPalindrome(palindromeStr):
    # Write your code here
    mylist=list()
    for i in range(len(palindromeStr)):
        temp=palindromeStr
        if palindromeStr[i]!='a':
            #temp[i]='a'
            temp2 = str(temp[:i])+"a"+str(temp[i+1:])
            if not checkpalin(temp2):
                mylist.append(temp2)
    if not mylist:
        return "IMPOSSIBLE"
    ans = sorted(mylist)[0]
    return ans
  
#   For eg. Input: bab
#   Lists possible not palindrome : ['aab','baa']
#   Find the least of them -> 'aab'
