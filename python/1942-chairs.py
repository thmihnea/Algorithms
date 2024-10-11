from typing import List
import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        order = sorted(list(range(len(times))), key=lambda x: times[x][0])
        available_chairs = list(range(len(times)))
        used_chairs = []

        for i in range(len(order)):
            arrival, departure = times[order[i]]
            while used_chairs and used_chairs[0][0] <= arrival:
                element = heapq.heappop(used_chairs)
                heapq.heappush(available_chairs, element[1])
            
            chair = heapq.heappop(available_chairs)
            if order[i] == targetFriend:
                return chair
            
            heapq.heappush(used_chairs, (departure, chair))