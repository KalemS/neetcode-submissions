class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        visited = set()
        longest = 0

        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            total = 1
            while num+total in seen:
                visited.add(num+total)
                total += 1
            longest = max(total, longest)

        return longest
