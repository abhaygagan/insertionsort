def selectionsort(arr):
    for i in range(len(arr)-1):
        temp=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                temp=j
        arr[i],arr[temp]=arr[temp],arr[i]
    return arr

selectionsort([10,8,6,4,2])



def bubblesort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

bubblesort([10,8,6,4,2])



import random
def insertionsort(nums):
    for i in range(1,len(nums)):
        anchor=nums[i]
        j=i-1
        while j>=0 and anchor<nums[j]:
            nums[j+1]=nums[j]
            j=j-1
        nums[j+1]=anchor

nums=random.sample(range(0,30),5)
insertionsort(nums)
print(nums)
