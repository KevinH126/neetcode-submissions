class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value,timestamp)]
        else:
            self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        l = 0
        r = len(self.store[key])-1
        if timestamp > self.store[key][r][1]:
            return self.store[key][r][0]
        while l <= r:
            m = (l+r)//2
            if self.store[key][m][1] > timestamp:
                r = m-1
            elif self.store[key][m][1] < timestamp:
                l = m+1
            else:
                return self.store[key][m][0]
        return self.store[key][r][0] if r >= 0 else ""

