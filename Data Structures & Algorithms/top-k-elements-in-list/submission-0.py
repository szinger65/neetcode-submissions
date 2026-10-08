class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elems = defaultdict(int)
        for num in nums:
            elems[num] += 1
        sorted_d = dict(sorted(elems.items(), key=lambda item: item[1]))
        li = list(sorted_d.keys())
        return li[-k:]
            
            