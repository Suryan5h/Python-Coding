class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        unclosed=[]
        if(len(x))==1:
            return False
            
        for i in range(len(x)):
            if x[i] in (')','}',']'):
                if len(unclosed)!=0:
                    if (x[i]==')' and unclosed[-1]=='(') or (x[i]==']' and unclosed[-1]=='[') or (x[i]=='}' and unclosed[-1]=='{'):
                        unclosed = unclosed[:-1]
                    else:
                        return False
                else:
                    return False
            else:
                unclosed.append(x[i])
        if len(x)>0 and len(unclosed)==0:
            return True
        else:
            return False
