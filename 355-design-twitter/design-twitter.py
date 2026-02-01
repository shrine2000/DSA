class Twitter:
    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        pq, res = [], []
        self.followers[userId].add(userId)

        for followee in self.followers[userId]:
            tweets = self.tweetMap[followee]
            if tweets:
                time, tweetId = tweets[-1]
                idx = len(tweets) - 1
                heapq.heappush(pq, (-time, tweetId, followee, idx))
        while pq and len(res) < 10:
            _, tweetId, user, idx = heapq.heappop(pq)
            res.append(tweetId)

            if idx > 0:
                time, tweetId = self.tweetMap[user][idx - 1]
                heapq.heappush(pq, (-time, tweetId, user, idx - 1))
        return res

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
