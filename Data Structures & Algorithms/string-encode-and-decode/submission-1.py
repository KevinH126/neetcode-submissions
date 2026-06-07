class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for x in strs:
            output+=str(len(x))
            output+="%"
            output+=x
        return output
    def decode(self, s: str) -> List[str]:
        output = []
        k = 0
        i = 0
        while i < len(s):
            k = ""
            while s[i] != "%":
                k+=s[i]
                i+=1
            num=int(k)
            i+=1
            ss = ""
            while i < len(s) and num > 0:
                ss+=s[i]
                i+=1
                num-=1
            output.append(ss)
            
        return output