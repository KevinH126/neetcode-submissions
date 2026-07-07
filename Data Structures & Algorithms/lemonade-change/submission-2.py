class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0, 20:0}

        for x in bills:
            change[x] +=1
            if x > 5:
                togive = x-5
                while togive > 0 and change[10] > 0:
                    if togive-10 >= 0:
                        togive-=10
                        change[10] -=1
                    else:
                        break
                while togive > 0 and change[5] > 0:
                    togive-=5
                    change[5] -= 1
                if togive > 0:
                    return False
        return True

