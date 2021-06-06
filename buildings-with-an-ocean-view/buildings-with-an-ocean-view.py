class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_so_far = -1
        output = []
        for i in reversed(range(len(heights))):
            if heights[i] > max_so_far:
                max_so_far = heights[i]
                output.append(i)
        return reversed(output)