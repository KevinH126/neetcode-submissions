class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = 101
        second = 101

        for x in prices:
            if x < first:
                second = first
                first = x
            elif x < second:
                second = x
        leftover = money - first - second
        if leftover <0:
            return money
        return leftover