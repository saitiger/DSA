class Solution:
    def __init__(self):
        self.result = []

    def isSafe(self, i, j, n):
      # Valid index (Checking for out of bounds index)
        return 0 <= i < n and 0 <= j < n

    def solve(self, i, j, m, n, temp):
        if not self.isSafe(i, j, n) or m[i][j] == 0:
          # Is valid and path is not blocked 
            return

        if i == n - 1 and j == n - 1:
          # Reached the end 
            self.result.append(temp)
            return

        m[i][j] = 0  # Mark cell as visited

        # Explore Up, Down, Left, Right 
        self.solve(i + 1, j, m, n, temp + 'D')
        self.solve(i, j + 1, m, n, temp + 'R')
        self.solve(i - 1, j, m, n, temp + 'U')
        self.solve(i, j - 1, m, n, temp + 'L')

        m[i][j] = 1  # Backtrack: unmark the cell

    def findPath(self, m, n):
        self.result = []  # Clear results before new run
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return []

        self.solve(0, 0, m, n, "")
        return self.result
