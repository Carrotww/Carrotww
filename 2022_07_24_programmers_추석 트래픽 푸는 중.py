import collections
from typing import List

def solution(lines):
    result = ''
    log_line = [[a, b, c] for a, b, c in [x.split() for x in lines]]

    def total_time(line: List) -> int:
        if not line:
            return 0
        log_Hour = int(line[1].split(":")[0])
        log_min = int(line[1].split(":")[1])
        log_sec = int(line[1].split(":")[2].split(".")[0])
        log_msec = int(line[1].split(":")[2].split(".")[1])

        return log_msec + (log_sec * 100) + (log_min * 6000) + (log_Hour * 360000)

    return total_time(log_line[0])

li = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]

print(solution(li))