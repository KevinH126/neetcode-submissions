class Twitter:

    def __init__(self):
        self.users = {} # user : {tweets: [], news: [], followers: []}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {"tweets": [], "following": set()}
            self.users[userId]["following"].add(userId)
        self.users[userId]["tweets"].append([self.time,tweetId])
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.users[userId] = {"tweets": [], "following": set()}
        heap = []
        for x in self.users[userId]["following"]:
            for tweet in self.users[x]["tweets"]:
                heapq.heappush_max(heap,tweet)
        
        output = []
        for i in range(10):
            if not heap:
                break
            time, tweetId = heapq.heappop_max(heap)
            output.append(tweetId)
        return output
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = {"tweets": [], "following": set()}
            self.users[followerId]["following"].add(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = {"tweets": [], "following": set()}
            self.users[followeeId]["following"].add(followeeId)
        self.users[followerId]["following"].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = {"tweets": [], "following": set()}
        else:
            if followeeId in self.users[followerId]["following"]:
                self.users[followerId]["following"].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)