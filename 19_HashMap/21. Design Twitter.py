# https://leetcode.com/problems/design-twitter/


class Twitter:

    def __init__(self):
        self.tweets = []
        self.following = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        i = len(self.tweets)-1
        while i >= 0 and len(res) < 10:
            u, t = self.tweets[i]
            if u == userId or u in self.following[userId]:
                res.append(t)
            i -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
if __name__ == "__main__":
    twitter = Twitter()
    
    # User 1 posts a tweet
    twitter.postTweet(1, 5)
    
    # User 1's news feed should return [5]
    print(twitter.getNewsFeed(1))  # Output: [5]
    
    # User 1 follows user 2
    twitter.follow(1, 2)
    
    # User 2 posts a tweet
    twitter.postTweet(2, 6)
    
    # User 1's news feed should return [6, 5]
    print(twitter.getNewsFeed(1))  # Output: [6, 5]
    
    # User 1 unfollows user 2
    twitter.unfollow(1, 2)
    
    # User 1's news feed should return [5]
    print(twitter.getNewsFeed(1))  # Output: [5]
