class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:


        restrictions.sort()
        prev = (1, 0)
        for i in range(len(restrictions)):
            if restrictions[i][0] - prev[0] + prev[1] < restrictions[i][1]:
                restrictions[i] = [restrictions[i][0], restrictions[i][0] - prev[0] + prev[1]] 
            prev = restrictions[i]    

        if restrictions:
            prev = restrictions[len(restrictions) - 1]
            for i in range(len(restrictions) - 2, -1, -1):
                if prev[1] + (prev[0] - restrictions[i][0]) < restrictions[i][1]:
                    restrictions[i] = [restrictions[i][0], prev[1] + (prev[0] - restrictions[i][0])] 
                prev = restrictions[i]
            
        prev = (1, 0)
        i = 0
        mx = 0
        while i < len(restrictions):

            if restrictions[i][0] - prev[0] + prev[1] < restrictions[i][1]:
                mx = max(mx, restrictions[i][0] - prev[0] + prev[1])
                prev = (restrictions[i][0], restrictions[i][0] - prev[0] + prev[1])
                i += 1
                continue

            if restrictions[i][1] < prev[1]:
                tmp = prev[1] - restrictions[i][1]
                total = restrictions[i][0] - prev[0] 
                total -= tmp
                mx = max(mx, prev[1] + (total) // 2)
            elif restrictions[i][1] > prev[1]:
                tmp = restrictions[i][1] - prev[1]
                total = restrictions[i][0] - prev[0] 
                total -= tmp
                mx = max(mx, restrictions[i][1] + (total) // 2)
            else:
                total = restrictions[i][0] - prev[0]  
                mx = max(mx, prev[1] + (total) // 2)

            prev = restrictions[i]
            i += 1

        end = n

        # print(mx, prev, end)

        mx = max(mx, prev[1] + end - prev[0])

        return (mx)

        
        