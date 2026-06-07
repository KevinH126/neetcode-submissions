class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        output = []
        carry = 1

        while i >= 0:
            sum = digits[i] +carry
            carry = sum//10
            output.append(sum%10)
            i-=1
        if carry:
            output.append(carry)
        output.reverse()
        return output