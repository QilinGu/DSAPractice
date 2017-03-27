class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = {}
        self.followees = {}
        self.order = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.order += 1
        if userId in self.tweets:
            self.tweets[userId].append((self.order, tweetId))
        else:
            self.tweets[userId] = [(self.order, tweetId)]
        # print self.tweets


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        feed = []
        if userId in self.tweets:
            feed = self.tweets[userId][-10:]
        if userId in self.followees:
            for followee in self.followees[userId]:
                if followee in self.tweets:
                    feed += self.tweets[followee][-10:]
        feed.sort(key=lambda x: x[0])
        return [ tweet[1] for tweet in feed[-10:][::-1] ]


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.followees:
            self.followees[followerId] = set()
        self.followees[followerId].add(followeeId)
        print self.followees


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.followees:
            return
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
        print self.followees


if __name__ == '__main__':

    res = []
    call = ["postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","postTweet","unfollow","postTweet","postTweet","postTweet","getNewsFeed","postTweet","postTweet","getNewsFeed","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","follow","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","follow","postTweet","postTweet","postTweet","postTweet","follow","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","postTweet","postTweet","getNewsFeed","postTweet","postTweet","follow","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","unfollow","postTweet","postTweet","unfollow","getNewsFeed","postTweet","postTweet","follow","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","unfollow","getNewsFeed","postTweet","postTweet","postTweet","unfollow","postTweet","postTweet","postTweet","postTweet","unfollow","postTweet","postTweet","postTweet","getNewsFeed","postTweet","postTweet"]
    para = [[11,994],[4,303],[1,113],[18,309],[8,905],[6,605],[1,210],[15,15],[1,88],[1,704],[8],[9,59],[4,851],[13,974],[2,133],[15,255],[15,662],[16,21],[13,227],[17],[5,603],[10,7],[5,816],[7,792],[12,260],[5],[4,586],[1,645],[20],[15,171],[16,18],[3,812],[15,153],[12,726],[6,508],[17,817],[5,6],[3,667],[5,599],[13,353],[11,282],[7,226],[18,423],[13,875],[2,738],[6,727],[7,374],[19,811],[8,418],[2,179],[3,476],[9,15],[16,8],[19,827],[17,203],[13,246],[14,8],[13,750],[4,595],[1,793],[17,995],[11,589],[2,115],[18,870],[15,426],[18,953],[10,318],[10,419],[2,164],[9],[18,854],[3,394],[17],[4,834],[4,349],[2,16],[13,534],[3,773],[4,292],[5,951],[17,554],[4,646],[6,412],[15,548],[8,188],[5,539],[18,732],[8,591],[11,733],[1,517],[8,156],[13,331],[11,889],[12,782],[11],[2,578],[16,487],[12,640],[14,112],[10,901],[8,807],[7,818],[7,627],[14,9],[4,522],[7,505],[9,13],[3],[1,971],[18,808],[1,17],[7,197],[7,361],[2,986],[17,6],[7,211],[15,342],[5,538],[1,711],[11,863],[17,339],[5,656],[4,402],[1,514],[11,566],[12,11],[12],[19,899],[19,526],[20,799],[4,1],[17,363],[7,845],[15,329],[17,369],[18,18],[15,848],[5,928],[18,105],[18],[17,785],[11,457]]
    call1 = ["postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
    para1 = [[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
    twitter = Twitter()
    dispatcher = {"postTweet": twitter.postTweet,
                  "getNewsFeed": twitter.getNewsFeed,
                  "follow": twitter.follow,
                  "unfollow": twitter.unfollow}
    i = 0
    while i < len(call):
        if call[i] == 'getNewsFeed':
            #res.append(dispatcher[call[i]](para[i][0]))
            print dispatcher[call[i]](para[i][0])
        else:
            #res.append(dispatcher[call[i]](para[i][0], para[i][1]))
            print dispatcher[call[i]](para[i][0], para[i][1])
        i += 1