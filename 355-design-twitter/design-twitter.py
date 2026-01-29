class Twitter:

    def __init__(self):
        self.tweetMap =defaultdict(list) 
        self.followers = defaultdict(set)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        self.followers[userId].add(userId)

        for followee in self.followers[userId]:
            tweets.extend(self.tweetMap[followee])
        
        tweets.sort(key=lambda x:x[0], reverse=True)
        return [tweetId for _, tweetId in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)