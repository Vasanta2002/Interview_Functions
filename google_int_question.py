"""Unique Paths

There is a robot on an 'm' x 'n' grid. The robot is initially located at the top-left corner.
The robot tries to move to the bottom-right corner. The robot can only move either down or
right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot 
can take to reach the bottom-right corner.
"""

def uniquePaths(self, m: int, n: int) -> int:
    """
    Calculate the number of unique paths for a robot to move from the top-left corner to
    the bottom-right corner of an 'm' x 'n' grid.

    Parameters:
        m (int): The number of rows in the grid.
        n (int): The number of columns in the grid.

    Returns:
        int: The number of possible unique paths.
    """
    
    # 1. Initialize Board of Zeros
    ret = []
    for i in range(m):
        ret.append([0] * n)

    # 2. Mark Top-Left as 1
    ret[0][0] = 1

    # 3. Fill the Board
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                ret[i][j] = ret[i][j - 1]
            else:
                ret[i][j] = ret[i][j - 1] + ret[i - 1][j]

    # 4. Return the Answer
    return ret[-1][-1]
