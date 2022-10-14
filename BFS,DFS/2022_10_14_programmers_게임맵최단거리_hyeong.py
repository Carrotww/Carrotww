# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 푸는 중

def solution(maps):
    result = []
    row_last = len(maps[0]) - 1
    col_last = len(maps) - 1
    
    def dfs(maps, row, col, cnt):
        if row == row_last and col == col_last:
            result.append(cnt)
            return
        if row > row_last or col > col_last:
            return
        if row + 1 <= row_last and maps[col][row + 1] == 1:
            temp = maps[:]
            temp[col][row + 1] = 0
            dfs(temp, row + 1, col, cnt + 1)
        if row - 1 >= 0 and maps[col][row - 1] == 1:
            temp = maps[:]
            temp[col][row - 1] = 0
            dfs(temp, row - 1, col, cnt + 1)
        if col + 1 <= col_last and maps[col + 1][row] == 1:
            temp = maps[:]
            temp[col + 1][row] = 0
            dfs(temp, row, col + 1, cnt + 1)
        if col - 1 >= 0 and maps[col - 1][row] == 1:
            temp = maps[:]
            temp[col - 1][row] = 0
            dfs(temp, row, col - 1, cnt + 1)
    
    dfs(maps, 0, 0, 1)

    if result:
        return min(result)
    return -1

print(solution([[1,0], [1,0], [1,0],[1,1]]))