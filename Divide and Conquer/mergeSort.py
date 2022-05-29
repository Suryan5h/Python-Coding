def merge(left,right):

    result =[]
    left_pointer = 0
    right_pointer = 0

    while left_pointer<len(left) and right_pointer<len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result

def mergesort(arr):

    if(len(arr)==1):
        return arr
    
    mid = len(arr)//2
    left, right = mergesort(arr[:mid]), mergesort(arr[mid:])
    return merge(left,right)


def main():
    arr=[1,3,5,-1,230,8,2,4]
    print(arr)
    result = mergesort(arr)
    print(result)

if __name__ == "__main__":
    main()
    
# Output:
# [1, 3, 5, -1, 230, 8, 2, 4]
# [-1, 1, 2, 3, 4, 5, 8, 230]
