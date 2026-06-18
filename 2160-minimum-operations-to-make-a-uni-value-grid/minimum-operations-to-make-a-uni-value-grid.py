class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                nums.append(grid[i][j])
        nums.sort()

        middle = len(nums) // 2
        rem = nums[0] % x
        ans = 0

        for num in nums:
            if num % x != rem:
                return -1
            # print(abs(middle - num) // x)
            ans += abs(nums[middle] - num) // x

        return ans





