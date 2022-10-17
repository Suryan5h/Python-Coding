def convertFive(n):
    # Code here
    n_str = str(n)
    newnum = ""
    for i in range(len(n_str)):
        if int(n_str[i])==0:
            newnum+="5"
        else:
            newnum+=n_str[i]
    return int(newnum)
