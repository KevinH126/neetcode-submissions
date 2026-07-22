class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        wordCounts = {}
        charCounts = Counter(chars)
        output = 0
        for x in words:
            wordCounts[x] = Counter(x)
            asdf = False
            for k,v in wordCounts[x].items():
                if k not in charCounts or charCounts[k] < v:
                    asdf = True
                    break
            if asdf:
                continue
            else:
                output += len(x)
        return output
                
            