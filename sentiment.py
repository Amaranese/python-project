import tweepy
from textblob import TextBlob


consumer_key = 'uRCxyoM8A0X8eyjvEzJ0EWhcS'
consumer_secret = '9aB543elAGHUVT1sXBIBweNrRR0K0SSgX5p5l7jg4NyCgkLANv'

access_token = '80632501-4sTASkQm6P4k6YvyjdtdxOcIEtZazD1ptyMSodXDY'
access_token_secret = 'QQ3Y32jKxo7OCwKNs016Ekkmf7ctTAChubYrsf3lrN5ok'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Fiji')


for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)