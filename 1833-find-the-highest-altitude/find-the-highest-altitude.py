class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = 0
        ans = 0

        for num in gain:
            prefix += num
            ans = max(ans, prefix)
        
        return ans