def getMinMax( a, n):
    import sys
    mini = maxi = a[0]
    for i in range(1,n):
        if mini>a[i]:
            mini=a[i]
        if maxi<a[i]:
            maxi=a[i]
    return [mini,maxi]
