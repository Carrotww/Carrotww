from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        start_list = list()
        for tic in tickets:
            if tic[0] == "JFK":
                for t in tic:
                    start_list.append(t)
                tickets.remove(tic)
        while tickets:
            temp_list = list()
            for i in tickets:
                if start_list[-1] == i[0]:
                    temp_list.append(i)
            temp_list.sort()
            start_list.append(temp_list[0][0])
            tickets.remove(temp_list[0])

        return start_list

a = Solution()
print(a.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))