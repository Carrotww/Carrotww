def solution(n, paths, gates, summits):
    temp = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        temp[i].append((j, w))
        temp[j].append((i, w))

    min_dis = [10000001 for _ in range(n + 1)]

    return 1

n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]

solution(n, paths, gates, summits)