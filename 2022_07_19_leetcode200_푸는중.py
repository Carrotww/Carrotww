from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid[0]), len(grid)
        check_list = []
        cnt = 0

        def fun1(c, r):
            i = 0
            while grid[c + i][r] == "1" and [c + i, r] not in check_list:
                check_list.append([c + i, r])
                i += 1
                j = 0
                if c + i < len(grid):
                    break
                while grid[c][r + j] == "1" and [c, r + j] not in check_list:
                    check_list.append([c, r + j])
                    j += 1
                    if r + j < len(grid[0]):
                        break
        for x in range(col):
            for y in range(row):
                ch_len = len(check_list)
                fun1(x, y)
                if ch_len != len(check_list):
                    cnt += 1

        return cnt

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