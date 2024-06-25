def quickSort(nums):
    if len(nums) <=1 :
        return nums
    pivot = nums[len(nums) // 2]
    left = [num for num in nums if num < pivot]
    right = [num for num in nums if num > pivot]
    mid = [num for num in nums if num == pivot]

    return quickSort(left) + quickSort(mid) + quickSort(right)
