import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        # Initialize heap with the first window
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        max_li = [-heap[0][0]]

        # Slide the window
        for r in range(k, len(nums)):
            left = r - k + 1

            # Add new element
            heapq.heappush(heap, (-nums[r], r))

            # Remove elements outside the window
            while heap and heap[0][1] < left:
                heapq.heappop(heap)

            # Get current maximum
            max_li.append(-heap[0][0])

        return max_li
            
