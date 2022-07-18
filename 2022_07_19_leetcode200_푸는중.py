from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid[0]) - 1, len(grid) - 1
        cnt = 0
        def fun1(x, y):
            while True:


        fun1(0, 0)

        return grid

a = Solution()

b = [[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
], [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]]

for i in b:
    print(a.numIslands(i))