def selectionsort(arr):
    for i in range(len(arr)-1):
        temp=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                temp=j
        arr[i],arr[temp]=arr[temp],arr[i]


selectionsort([10,8,6,4,2])
print(arr) 