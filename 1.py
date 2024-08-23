class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        n = len(temperatures)
        ans = [0] * n
        for i in range(n - 1, -1, -1):        
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()
            if stk:
                j = stk[-1]
                ans[i] = j - i
            stk.append(i)
        return ans
