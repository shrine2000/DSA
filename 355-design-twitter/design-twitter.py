class Twitter:

    def __init__(self):
        self.tweets_by_user = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.timestamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets_by_user[userId].append((self.timestamp, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follow_map[userId] | {userId}
        max_heap = []
        for uid in followees:
            tweets = self.tweets_by_user[uid]
            if tweets:
                index = len(tweets) - 1
                timestamp, tid = tweets[index]
                heapq.heappush(max_heap, (-timestamp, uid, index))

        result = []
        while max_heap and len(result) < 10:
            neg_time, uid, idx = heapq.heappop(max_heap)
            result.append(self.tweets_by_user[uid][idx][1])
            if idx > 0:
                prev_time, prev_tid = self.tweets_by_user[uid][idx - 1]
                heapq.heappush(max_heap, (-prev_time, uid, idx -1))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)