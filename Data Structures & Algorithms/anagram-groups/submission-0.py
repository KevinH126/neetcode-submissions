class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorts = collections.defaultdict(list)

        for x in strs:
            sorte = "".join(sorted(x))
            sorts[sorte].append(x)
        output = []
        for x in sorts.values():
            output.append(x)
        return output