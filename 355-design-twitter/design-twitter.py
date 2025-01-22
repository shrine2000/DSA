class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        _time = time.time()
        self.tweets[userId].append((_time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # get from user tweets
        pq = []
        for tweet in self.tweets[userId]:
            heapq.heappush(pq, tweet)
            if len(pq) > 10:
                heapq.heappop(pq)

        # get tweet from following
        for followee in self.following[userId]:
            for tweet in self.tweets[followee]:
                heapq.heappush(pq, tweet)
                if len(pq) > 10:
                    heapq.heappop(pq)
        return [tweetId for _, tweetId in sorted(pq, reverse=True)]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)