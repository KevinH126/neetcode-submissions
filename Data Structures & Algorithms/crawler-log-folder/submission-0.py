class Solution:
    def minOperations(self, logs: List[str]) -> int:
        output = 0 

        for x in logs:
            if x == '../':
                if output > 0:
                    output -=1
            elif x == './':
                continue
            else:
                output+=1
        return abs(output)