class Solution:
    def getSum(self, a: int, b: int) -> int:
        output = 0
        carry = 0

        for i in range(32):
            bita = (a >> i) & 1
            bitb = (b >> i) & 1

            sum_bit = bita ^ bitb ^ carry

            output |= (sum_bit << i)

            carry = (bita & bitb) | (bita & carry) | (bitb & carry)

        mask = 0xFFFFFFFF
        if output > 0x7FFFFFFF:
            output = ~(output ^ mask)
        return output

