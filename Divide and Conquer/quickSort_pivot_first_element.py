def partition(arr,low,high):
    pivot=arr[low]
    start=low
    end=high
    print("Pivot:",pivot)
    while start<end:
        while start<=end and arr[start]<=pivot:
            #Here start<=end is important for the case 67,56| (right side of pivot always smaller) 
            #and start index would keep on adding and go out of range.
            start+=1

        while start<=end and arr[end]>pivot:
            end-=1
        
        if(start<end):
            arr[start],arr[end] = arr[end],arr[start]
    
    arr[low],arr[end] = arr[end],arr[low]
    return end;

def quicksort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        #print("Pivot",arr[pi])
        #print("left :", arr[low:pi])
        #print("right :",arr[pi+1:high+1])
        print(arr)
        #print(low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

def main():
    arr=[10,11,124,12,34,99,9,5]
    quicksort(arr,0,len(arr)-1)
    print("Output:{}".format(arr))

if __name__ == "__main__":
    main()

# Pivot: 10
# [9, 5, 10, 12, 34, 99, 124, 11]
# Pivot: 9
# [5, 9, 10, 12, 34, 99, 124, 11]
# Pivot: 12
# [5, 9, 10, 11, 12, 99, 124, 34]
# Pivot: 99
# [5, 9, 10, 11, 12, 34, 99, 124]
# Output:[5, 9, 10, 11, 12, 34, 99, 124]
