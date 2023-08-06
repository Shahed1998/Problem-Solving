# ----------------------------------------------------------
# My solution
# ----------------------------------------------------------
# def removeElement(nums, val):
#     if len(nums) == 0:
#         return 0

#     if len(nums) == 1:
#         if nums[0] == val:
#             return 0
#         return 1

#     # Pointers
#     right = len(nums)-1
#     # Return
#     k = 0

#     for i in range(len(nums)):
#         if not val == nums[i]:
#             k += 1

#     for i in range(k):
#         if right == k-1:
#             break
#         elif (not nums[i] == val) and (nums[right] == val):
#             right -= 1
#         elif (nums[i] == val) and (not nums[right] == val):
#             nums[i] = nums[right]
#             right -= 1
#         elif nums[i] == val and nums[right] == val:
#             while True:
#                 right -= 1
#                 if nums[i] == val and not nums[right] == val:
#                     nums[i] = nums[right]
#                     nums[right] = val
#                     break
#     return k

# ----------------------------------------------------------
# LeetCode solution
# ----------------------------------------------------------

def removeElement(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


print(removeElement([3, 2, 2, 3], 3))
