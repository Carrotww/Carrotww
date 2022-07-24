import collections
import datetime

def solution(lines):
    answer = 0
    result = collections.defaultdict(list)
    re_line = [i.split() for i in lines]
    for i in range(len(re_line)):
        re_line[i] = [re_line[i][0] + ' ' + re_line[i][1], re_line[i][2].split("s"[0])]
    if len(lines) == 1:
        return 1
    start_time = re_line[0][0] - datetime.timedelta(seconds=int(re_line[0][1]))
    last_time = re_line.pop()[0]

    return last_time