"""Twitter Analysis."""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

ACCESS_TOKEN = "access-token"
ACCESS_TOKEN_SECRET = "access-secret"
API_KEY = "api-key"
API_SECRET = "api-secret"


class StdOutListener(StreamListener):
    """This is a basic listener that just prints received tweets to stdout."""

    def on_data(self, data):
        """On data."""
        print data
        return True

    def on_error(self, status):
        """On error."""
        print status

listener = StdOutListener()
auth = OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream = Stream(auth, listener)

try:
    stream.filter(track=['metoo'], async=True, stall_warnings=True)
except:
    print "Restarting..."
    stream.filter(track=['metoo'], async=True, stall_warnings=True)
