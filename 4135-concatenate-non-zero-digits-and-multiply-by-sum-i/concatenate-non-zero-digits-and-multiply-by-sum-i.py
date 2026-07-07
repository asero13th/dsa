class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        summ = 0
        arr = []
        for char in str(n):
            if char != "0":
                summ += int(char)
                arr.append(char)
        
        

        ans = int("".join(arr)) * summ
        return ans

