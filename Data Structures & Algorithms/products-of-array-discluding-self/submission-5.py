class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        fix = 1
        for i in range(n):
            answer[i] = fix
            fix *= nums[i]
        fix = 1
        for i in range(n-1,-1,-1):
            answer[i] *= fix
            fix *= nums[i]
        
        return answer