def bubbleSort(nums):
    for i in range(len(nums)-1, 0 , -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                # j is index, [j] is jth value
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
nums = [5, 3, 8, 6, 7, 2]
bubbleSort(nums)
print(nums)