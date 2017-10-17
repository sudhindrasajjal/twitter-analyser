"""Twitter Analysis."""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

ACCESS_TOKEN = "84054662-kiW3PoweiZxxKydJf3g8J7PfZdSP8xKRajYJIbLTe"
ACCESS_TOKEN_SECRET = "qf6Ruz5m1FCtZRmQfgu1pbjyIkNaeQaiMZX5CfyFbIc1T"
API_KEY = "Q3PU20jlz1HGACxMhOx4OF4pR"
API_SECRET = "JjYS4Qgu0fZMWGvHFNWfy5hxrQFSeT7LqLOqnaSfhrhC5nGMbU"

# f = open("tweets.txt", "a+")


class StdOutListener(StreamListener):
    """This is a basic listener that just prints received tweets to stdout."""

    def on_data(self, data):
        """On data."""
        print data
        # f.write(data)
        return True

    def on_error(self, status):
        """On error."""
        print status
        # f.close()


listener = StdOutListener()
auth = OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream = Stream(auth, listener)

try:
    stream.filter(track=['metoo'], async=True, stall_warnings=True)
except:
    print "Restarting..."
    stream.filter(track=['metoo'], async=True, stall_warnings=True)
