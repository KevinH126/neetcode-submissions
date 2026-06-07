class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordLength = len(beginWord)
        wordSet = set(wordList)
        queue = deque([(beginWord, 1)])

        while queue:
            currWord, seqLength = queue.popleft()
            for x in list(wordSet):
                diffs = sum(1 for i in range(wordLength) if x[i] != currWord[i])
                if diffs == 1:
                    if x == endWord:
                        return seqLength + 1
                    wordSet.remove(x)
                    queue.append((x, seqLength + 1))

        return 0



