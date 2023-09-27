# from tweepy import OAuthHandler
# from tweepy.streaming import StreamListener
import tweepy
import pandas as pd
import time




class Scrape ():
	def __init__(self, args):	
		self.consumer_key = "M7eKY4bsRvo5A4g8HHsoWIXWG"
		self.consumer_secret = "dzNnCQ9RzuL84IZns0oJoJQDNOpHCiar2kFGNHmhW32IMElD5e"
		self.access_token = "1305327779496431617-dy5C4B7nrn6XNMhGdAkL87svE8jajS"
		self.access_token_secret = "LYYFK6SiOdZMiWuCQYrsA0sNPA4RrldtuKoGLkjzGKTFy"
  
		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_token_secret)
		self.api = tweepy.API(self.auth,wait_on_rate_limit=True)

		self.text_query = args.Q
		#filter retweets removes retweets from scrape/ show only tweets 
		self.real_query = self.text_query + " -filter:retweets"
		self.fileOut = args.O
		self.finalFile = self.fileOut + ".html"
		print (self.finalFile)
		self.count = args.X
		try:
			# Creation of query method using parameters --> to show top tweets here, add "result_type='popular'"" after lang command separated by a comma
			tweets = tweepy.Cursor(self.api.search_tweets, q=self.real_query, lang = 'en').items(self.count)
			print ("Scraping for your data!")

			# Pulling information from tweets iterable object
			tweets_list = [[tweet.created_at, tweet.id, tweet.text, tweet.user.screen_name, tweet.favorite_count, tweet.retweet_count] for tweet in tweets]
			# Creation of dataframe from tweets list
			# Add or remove columns as you remove tweet information
			pd.set_option('display.max_rows', None)
			pd.set_option('display.max_columns', None)
			pd.set_option('display.width', None)
			pd.set_option('display.max_colwidth', None)        
			tweets_df = pd.DataFrame(tweets_list, columns = ['date','id', 'tweet', 'user', 'likes', 'retweets'])
			tweets_df.to_html(self.finalFile)
			
			#tweets_df = pd.DataFrame(tweets_list)
			print ("Congratulations! That worked. Check results in 'scrapeOutput.html file. Rename this folder before scraping again otherwise data will be lost!")
		
		#print error message 
		except BaseException as e:
			print('failed on_status,',str(e))
			time.sleep(3)