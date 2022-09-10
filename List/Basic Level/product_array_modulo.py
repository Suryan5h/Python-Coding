# arr is the array
# n is the number of element in array
# mod= modulo value
def product(arr,n,mod):
    # your code here
    from functools import reduce
    product = reduce(lambda x,y:x*y, arr)
    return product%mod
