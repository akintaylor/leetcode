from heapq import heapify, heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        free_laptops = []

        heapify(free_laptops)

        intervals.sort(key=lambda x: x[0])
        heappush(free_laptops, intervals[0][1])

        for time in intervals[1:]:
            if free_laptops[0] <= time[0]:
                heappop(free_laptops)
                
            heappush(free_laptops, time[1])

        return len(free_laptops)
