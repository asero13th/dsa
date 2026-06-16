class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        for idx, num in enumerate(nums):
            hashmap[num].append(idx)
        ans = float('inf')
        for key, val in hashmap.items():
            if len(val) >= 3:
                i, j, k = 0, 1, 2

                while k < len(val):
                    window = abs(val[i] - val[j]) + abs(val[j] - val[k]) + abs(val[k] - val[i])
                    ans = min(ans, window)

                    i += 1
                    j += 1
                    k += 1
        return ans if ans != float('inf') else -1