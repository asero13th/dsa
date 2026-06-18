class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        rem = grid[0][0] % x
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] % x != rem:
                    return -1
                nums.append(grid[i][j])
                
        nums.sort()
        middle = len(nums) // 2
        
        ans = 0

        for num in nums:
            ans += abs(nums[middle] - num) // x

        return ans
