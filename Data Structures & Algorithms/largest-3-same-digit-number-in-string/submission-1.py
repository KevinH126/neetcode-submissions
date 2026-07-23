class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = "-1"
        found = False

        for i in range(len(num)-2):
            poo = num[i:i+3]
            if len(set(poo)) == 1 and int(poo) > int(largest):
                largest = poo
                found = True
        if found:
            return largest
        return ""