#!/usr/bin/python

from __future__ import print_function
from time import localtime, strftime
import twitter
import itertools
import random
import time
import datetime
from datetime import timedelta
from engage_settings_chakra import *

def check_description_and_follow(api, user, bio_kws, city):
	# Check if user description (bio/title) contains keywords in bio_kws list, 
	# following them if they live in Portland.
	for word in bio_kws:
		if word in user.description and user.location==city:
			#follow user
			api.CreateFriendship(user.id)
			print("Befriended: %s" % user.screen_name)

def check_status_and_favorite(api, user, post_kws):
	for word in post_kws:
		#get status
		statuses = api.GetUserTimeline(user.id)
		for status in statuses:
			if word in status.text:
				api.CreateFavorite(status)
				print("Favorited Status from: %s" % status.user.screen_name)

def get_followers(targets):
	# Return list of users that are followers of targets.
	users = []
	for target in targets:
		users = users + api.GetFriends(target)
	return users

def sleep(time, seconds):
	# Create a random time delay between 0 and 10 seconds
	delay = random.randint(1,seconds)
	print("Sleeping for %d seconds." % delay)
	time.sleep(delay)

def create_query_words(keywords):
	query_words = []
	for i in range(1,4):
		results = []
		results += [" ".join(list(tup)) for tup in itertools.combinations(keywords, i)]
		query_words += results
	return query_words

def create_queries(query_words):
	query_list = []
	for term in query_words:
		new_term = term.replace(' ','%20') + '%20'
		# city = '''near%3A"Portland%2C%20OR"%20within%3A50mi%20'''
		raw_query = '''q=%snear%3A"Portland%2C%20OR"%20within%3A15mi\%20\since%3A2017-11-01&src=typd''' % new_term
		query_list.append(raw_query)
	return query_list

def add_to_query_list(query, query_list):
	if query not in query_list:
		query_list[query] = 1
	else:
		query_list[query] += 1
	return query_list

if __name__ == '__main__':
	print("*** Welcome to TweetBot ***")
	print(strftime("Gathering Users: %a, %d %b %Y %H:%M:%S", localtime()))

	# Get a ton of queries based on keywords, find matching tweets, like tweets.
	# terms = create_query_words(post_kws)
	terms = post_kws + bio_kws
        random.shuffle(terms) #Randomize this for every time through.
	geo_code = '45.52307063819725,-122.67630636692047,100mi'
	today = datetime.date.today()
	month_ago = (today-timedelta(days=30)).strftime('%Y-%m-%d')
	for term in terms:
		print("Searching for tweets of term: %s" % term)
		tweets = api.GetSearch(term=term, since=month_ago)
		print("tweets", tweets)
		print("%d tweets found for term: %s" % (len(tweets), term))	
		for tweet in tweets:
			try:
				api.CreateFavorite(tweet)
				print("liked tweet from %s" % tweet.user.screen_name)
				delay = random.randint(1,60)
				print("Post Favorite Sleep for %d seconds." % delay)
				time.sleep(delay)
			except:
				print(strftime("Reached Rate Limit. Waiting 15 minutes: %a, %d %b %Y %H:%M:%S", localtime()))
				time.sleep(900)


	# # TODO Save the user objects in a local cache/file (include at least user id and screen_name)
	# my_friends = api.GetFriends() # Get a list of users I follow.
	# print('Number of users found: ', len(my_friends))
	# for user in my_friends:
	# 	try:
	# 		# At the Start of actions print time.
	# 		print(strftime(("Engaging: " + user.screen_name + " %a, %d %b %Y %H:%M:%S"), localtime()))
	# 		delay = random.randint(1,10)
	# 		print("Sleeping for %d seconds." % delay)
	# 		time.sleep(delay)
	# 		# check_description_and_follow(api, user, bio_kws, city)
	# 		# Check if any posts match our keywords, if so favoriting the post.
	# 		check_status_and_favorite(api, user, post_kws)
	# 	except:
	# 		print("Already liked this message/skipped:")

		
