class Twitter:
    from heapq import heapify, heappop
    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.data = defaultdict(list)
        self.timestamp = 0
        self.follows = defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.follows[userId]:
            self.follows[userId].add(userId)
        self.data[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feed = []
        for person in self.follows[userId]:
            feed.extend(self.data[person])
        heapify(feed)
        ans = []
        for i in range(min(10, len(feed))):
            ans.append(heappop(feed)[1])
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
