if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([score,name])
    
    #print(l)
    l = sorted(l)
    for i in range(1,len(l)):
        if l[i][0]>l[0][0]:
            value=l[i][0]
            break
        
    for val in range(1,len(l)):
        if l[val][0]==value:
            print(l[val][1])
    #print(l)
