"""Search an array for a target in log n time.
The list must be sorted in order of smallest to biggest."""

List = [-9, -4, -2, 1, 5, 8, 9]
target = 5

def search(nums: [], target: int):
    l = 0
    r = len(nums)-1


    while l <= r:
        m = (l+r)//2

        if target == nums[m]:
            return m
        elif target < nums[m]:
            r = m-1
        elif target > nums[m]:
            l = m+1

    return -1 # Time: O(log(n)), Space: 0(1)

print(search(List, target))

