class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # sorted array
        # 1, 2, 3, 4

        l, r = 0, len(numbers) - 1

        while l < r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l + 1, r + 1]
            if summ < target:
                l += 1
            else:
                r -= 1