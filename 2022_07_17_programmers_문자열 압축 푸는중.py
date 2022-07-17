import collections

def solution2(s):
    str_dict = collections.defaultdict(int)
    result = collections.defaultdict(list)
    max_len = len(s) // 2

    for i in range(1, max_len + 1):
        for p in range(0, len(s), i):
            start = p
            end = p + i
            end2 = i + (p + i)
            s1 = s[start:end]
            s2 = s[end:end2]
            if s[start:end] == s[end:end2]:
                str_dict[i] += 1

    if not str_dict:
        return s

    return str_dict

def solution(s):
    max_len = len(s) // 2
    return min(solution2(s, max_len))

a = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", \
     "xababcdcdababcdcd"]
for i in a:
    print(solution(i))