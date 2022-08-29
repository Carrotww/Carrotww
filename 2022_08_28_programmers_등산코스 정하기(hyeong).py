import heapq

def solution(n, paths, gates, summits):
    temp = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        temp[i].append((j, w))
        temp[j].append((i, w))

    # 다익스트라
    pq = [(0, gate) for gate in gates] # 현재 경로의 intensity와 현재 지점
    # heap 정렬을 해야 하므로 heapq로 빼고 넣어야함
    min_dis = [10000001 for _ in range(n + 1)]

    while pq:
        intensity, node = heapq.heappop(pq)
        if min_dis[node] <= intensity:
            continue
        min_dis[node] = intensity
        for next_val, next_len in temp[node]:
            # next_val -> 다음 node의 number
            # next_len -> 다음 node까지의 거리
            next_len = max(intensity, next_len)
            if min_dis[next_val] <= next_len:
                continue
            heapq.heappush(pq, (next_len, next_val))

    # temp
    # []
    # [(2, 3)]
    # [(1, 3), (3, 5), (4, 2), (5, 4)]
    # [(2, 5), (4, 4)]
    # [(2, 2), (3, 4), (5, 3), (6, 1)]
    # [(2, 4), (4, 3), (6, 1)]
    # [(4, 1), (5, 1)]
    # min_dis
    # [10000001, 10000001, 10000001, 10000001, 10000001, 10000001, 10000001]


n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]

solution(n, paths, gates, summits)