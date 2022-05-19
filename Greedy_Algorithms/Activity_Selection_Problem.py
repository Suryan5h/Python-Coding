def printMaxActivities(s,e):
    n=len(e)
    print("The following activities are selected")

    #First activity is always selected
    i=0
    print(i,end=' ')

    for j in range(1,n):
        if s[j]>=e[i]:
            print(j,end = ' ')
            i=j

def main():
    s = [1 , 3 , 0 , 5 , 8 , 5]
    e = [2 , 4 , 6 , 7 , 9 , 9]

    printMaxActivities(s,e)

if __name__ == "__main__":
    main()
    
