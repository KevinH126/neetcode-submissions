class Solution:
    def minimumPushes(self, word: str) -> int:
        chars = Counter(word)

        arr = [[] for i in range(len(word)+1)]
        for letter, count in chars.items():
            arr[count].append(letter)
        
        count = 0
        seen = 0
        for i in range(len(arr)-1,-1,-1):
            if len(arr[i]) > 0:
                for x in arr[i]:
                    count += ((seen//8) + 1)*i
                    seen+=1
        return count