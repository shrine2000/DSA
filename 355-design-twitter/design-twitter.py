class Twitter:

    def __init__(self):
        self.follower = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timer = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1

        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        followees = self.follower[userId] | {userId}
        for followee in followees:
            for t, Id in self.tweets[followee][-10:]:
                heapq.heappush(heap, (t, Id))
                if len(heap) > 10:
                    heapq.heappop(heap)
        return [id for _,id in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)