class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            found_diff = False
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    found_diff = True
                    break
            if not found_diff and len(w1) > len(w2):
                return ""          # w2 is a strict prefix of w1 → invalid

        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            c = q.popleft()
            res.append(c)
            for nxt in adj[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        if len(res) < len(adj):
            return ""              # a cycle remained → no valid ordering
        return "".join(res)


