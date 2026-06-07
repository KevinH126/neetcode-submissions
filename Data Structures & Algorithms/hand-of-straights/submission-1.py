class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        numGroups = int(len(hand) / groupSize)
        hand = sorted(hand)

        straights = [[] for i in range(numGroups)]

        idx = 0
        straights[0].append(hand[0])
        for i in range(1,len(hand)):
            if hand[i-1] == hand[i]:
                idx += 1
            else:
                idx = 0
            while idx < numGroups and len(straights[idx]) == groupSize:
                idx+=1
            if idx >= numGroups:
                return False
            if len(straights[idx]) > 0 and hand[i] - straights[idx][-1] > 1:
                return False
            straights[idx].append(hand[i])
        return True