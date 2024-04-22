"""Search an array for a target in log n time.
The list must be sorted in order of smallest to biggest."""
def search(nums: [], target: int):
    """
    Search for a target in a sorted array using a binary search algorithm.

    Parameters:
        nums (list): A sorted list of integers.
        target (int): The integer to search for in the list.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if target == nums[m]:
            return m
        elif target < nums[m]:
            r = m - 1
        elif target > nums[m]:
            l = m + 1

    return -1  # Time: O(log(n)), Space: O(1)

List = [-9, -4, -2, 1, 5, 8, 9]
target = 5
print(search(List, target))
