if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans = list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n)
    print(ans)

    #List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
