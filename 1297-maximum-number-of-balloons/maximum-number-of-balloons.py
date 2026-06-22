class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        ans = len(text)
        for char in "balon":
            if char in "lo":
                ans = min(ans, count[char]// 2)
            else:
                ans = min(ans, count[char])
        return ans