class TweetCounts:
    from collections import defaultdict

    def __init__(self):
        self.data = defaultdict(list)


    def recordTweet(self, tweetName: str, time: int) -> None:
        self.data[tweetName].append(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            step = 60
        elif freq == 'hour':
            step = 3600
        elif freq == 'day':
            step = 86400
        ans = []
        for i in range(startTime, endTime+1, step):
            ans.append(0)
        for record in self.data[tweetName]:
            if startTime <= record <= endTime:
                ans[(record-startTime)//step] += 1
        return ans
