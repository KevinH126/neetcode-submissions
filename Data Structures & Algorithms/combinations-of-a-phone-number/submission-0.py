class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        output = []

        def dfs(i, curr):
            if i == len(digits):
                if len(curr) > 0: output.append(curr)
                return
            
            for ch in mappings[digits[i]]:
                dfs(i+1, curr+ch)
            return

        dfs(0, "")
        return output