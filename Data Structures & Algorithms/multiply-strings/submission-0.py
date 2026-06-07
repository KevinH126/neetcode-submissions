class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int1 = 0
        int2 = 0
        
        curr = len(num1)-1
        for c in list(num1):
            dig = ord(c)-48
            int1+=dig*(10**curr)
            curr-=1
        curr = len(num2)-1
        for c in list(num2):
            dig = ord(c)-48
            int2+=dig*(10**curr)
            curr-=1
        
        return str(int1*int2)