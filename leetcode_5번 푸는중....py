from collections import deque
import copy

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = deque(s)
        ss = copy.deepcopy(s)
        result_1 = list()
        while s:
            if list(s) == list(s)[::-1]:
                result_1.append(s)
                break
            elif not s:
                break
            s.pop()
            if list(s) == list(s)[::-1]:
                result_1.append(s)
                break
            elif not s:
                break
            s.popleft()
        while ss:
            if list(ss) == list(ss)[::-1]:
                result_1.append(ss)
                break
            elif not ss:
                break
            ss.popleft()
            if list(ss) == list(ss)[::-1]:
                result_1.append(ss)
                break
            elif not ss:
                break
            ss.pop()
        if not result_1:
            return ''.join(s)
        return ''.join(max(result_1))

a = Solution()

print(a.longestPalindrome("babad"))
print(a.longestPalindrome("ccc"))
print(a.longestPalindrome("abb"))