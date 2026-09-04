class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flightmap = defaultdict(dict)
        for frm, to, price in flights:
            flightmap[frm][to] = price
        dp = {} # node, stop: cheapest to dest

        def dfs(node,stop, visited):
            if node == dst:
                return 0
            if stop > k or node in visited:
                return 1e9
            if (node,stop) in dp:
                return dp[(node,stop)]
            cheapest = 1e9
            visited.add(node)
            for to in flightmap[node]:
                cheapest = min(cheapest, flightmap[node][to] + dfs(to, stop+1, visited))
            visited.remove(node)
            dp[(node,stop)] = cheapest
            return cheapest
        cheapest = dfs(src,0, set()) 
        return -1 if cheapest == 1e9 else cheapest
        