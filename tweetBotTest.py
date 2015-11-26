import tweepy
import bitly_api

test_url = "http://133.130.102.214/articles/output.txt"

class TwitterAPI:
	def __init__(self):
		consumer_key = "kC3zuTCFifj5M9Fr4ZFyRVXMk"
		consumer_secret = "EmhojuBni8qY5TklnHDX00cWC5JHkRSD2WXSnzshSnz4cyK2gj"
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		access_token = "4274083937-YIO1aZI3C4cYbdC3nxkgmmeb3QWjfCTVqdqZ8Ef"
		access_token_secret = "MQgfFPCtgqNhKK1haRymc9UKNn4xmPCGv2H6MXyuGm1zb"
		auth.set_access_token(access_token, access_token_secret)
		self.api = tweepy.API(auth)

	def tweet(self, message):
		self.api.update_status(status=message)

def short_url(long_url):
	API_USER = "o_7u7i13pmiv"
	API_KEY = "R_a5cc6f2da9b14239b2e759e0eb8bc3c0"
	b = bitly_api.Connection(API_USER, API_KEY)	
	short_url = b.shorten(test_url)
	return short_url

if __name__ == "__main__":
	twitter = TwitterAPI()
	res_url = short_url(test_url)['url']
	article = open("../var/www/html/articles/output.txt", "r");
	tweet = article.read(220)
	upload = tweet + ".." + str(res_url)
	print upload
	twitter.tweet(upload)
	article.close()
