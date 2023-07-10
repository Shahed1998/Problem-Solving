# Time complexity of merging = 0(n)

def merge(nums1, m, nums2, n):
    # Constraint 1
    if not len(nums1) == m+n:
        return
    # Constraint 2
    elif not len(nums2) == n:
        return
    # Constraint 3
    elif (not m >= 0) or (not n <= 200):
        return
    # Constraint 4
    elif (not m+n >= 0) or (not m+n <= 200):
        return

    temp = []

    # this is used to ignore the zeroes in num1 array
    for i in range(m):
        temp.append(nums1[i])

    # i = pointer of temp array, j = pointer of num2 array
    i = j = 0
    numsList = []

    # temp = [1,2,3]
    # num2 = [2,5,6]
    while i < m and j < n:
        if temp[i] < nums2[j]:
            numsList.append(temp[i])
            i += 1
        elif temp[i] == nums2[j]:
            numsList.append(temp[i])
            numsList.append(nums2[j])
            i += 1
            j += 1
        elif temp[i] > nums2[j]:
            numsList.append(nums2[j])
            j += 1

    # checks after one array or both are exhausted
    while i < m:
        numsList.append(temp[i])
        i += 1

    while j < n:
        numsList.append(nums2[j])
        j += 1

    # nums1 array is referenced
    for i in range(len(numsList)):
        nums1[i] = numsList[i]

    return nums1


print(merge([1], 1, [], 0))
