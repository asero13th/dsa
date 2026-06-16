class Solution:
    def processStr(self, s: str) -> str:
        stack = []

        for char in s:
            if  char.isalpha():
                stack.append(char)
            elif char == "*" and stack:
                stack.pop()
            elif char == "#" and stack:
                stack += stack
            elif char == "%":
                stack = stack[::-1]
        
        return "".join(stack)