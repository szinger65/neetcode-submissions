class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        biggest = 0
        while l < r:
            while r > l:
                leng = r - l
                area = leng * (min(heights[r],heights[l]))
                biggest = max(area, biggest)
                r-=1
            r = len(heights) -1   
            l += 1
        return biggest
