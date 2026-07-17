class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf") 

        for r in range(len(nums)):
            total += nums[r]
            while total >= target: #only starts the window when its size meets required target
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res