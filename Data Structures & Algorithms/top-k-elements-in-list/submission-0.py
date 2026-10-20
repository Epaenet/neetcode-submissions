class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_nums = sorted(freq, key=freq.get, reverse=True)
        return sorted_nums[:k]