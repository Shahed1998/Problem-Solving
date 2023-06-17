def twoSum(nums, target):
    if len(nums) < 2:
        return False

    # -----------------------------------------------
    # Brute force
    # -----------------------------------------------
    # for leftPtr in range(len(nums)-1):
    #     for rightPtr in range(leftPtr+1, len(nums), 1):
    #         if nums[leftPtr] + nums[rightPtr] == target:
    #             return [leftPtr, rightPtr]

    # ------------------------------------------------
    # Using Two Pass Hash Table
    # ------------------------------------------------
    store = {}
    n = len(nums)
    for i in range(n):
        store[nums[i]] = i

    for i in range(n):
        complement = target - nums[i]

        if complement in store and store[complement] != i:
            return [i, store[complement]]

    return []


print(twoSum([3, 2, 4], 6))
