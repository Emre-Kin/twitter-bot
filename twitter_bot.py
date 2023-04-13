# You can not use it because now twitter API need to be montly subscribe
# And this code need Twipy 3.8 not last version
import tweepy
import time
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# folow the follower bot
for follower in limit_handler(tweepy.Cursor(api.followers).items):
    if follower.name == 'followername':
        follower.follow()
    break

#like tweets bot
search_string = 'python'
numbersOfTweet = 2 

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweet):
    try:
        tweet.favorite()
        print('I like that tweet')
    except tweepy.TweepError as e:
        print(e.reason)