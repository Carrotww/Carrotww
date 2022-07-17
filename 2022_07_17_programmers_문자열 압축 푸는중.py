import collections

def solution2(s, cnt):
    str_list = ''
    str_dict = collections.defaultdict(int)
    for p in range(0, len(s), cnt):
        start = p
        end = p + cnt
        end2 = cnt + (p + cnt)
        s1 = s[start:end]
        s2 = s[end:end2]
        if s[start:end] == s[end:end2]:
            str_dict[s[start:end]] += 1

        else:
            str_list += s[start:end]

    return str_list

def solution(s):
    max_len = len(s) // 2
    return [min(x.append(solution2(s, i))) for x in max_len]

a = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", \
     "xababcdcdababcdcd"]
for i in a:
    print(solution(i))