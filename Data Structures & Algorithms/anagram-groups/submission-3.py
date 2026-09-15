class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            if tuple(count) not in groups:
                groups[tuple(count)] = [s]
            else:
                groups[tuple(count)].append(s)
        result = []
        for key,group in groups.items():
            result.append(group)
        return result