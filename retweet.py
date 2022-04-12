import tweepy 
from time import sleep 
from user_data import *
from config import FOLLOW, QUERY, SLEEP_TIME, LIKE

auth = tweepy.OAuthHandler(user_key, user_secret) 
auth.set_access_token(access_token_main, access_token_secret) 
api = tweepy.API(auth) 


def main():
    for tweet in tweepy.Cursor(api.search, q=QUERY).items(): 
        try: 
            print('\nTweet by: @' + tweet.user.screen_name) 

            tweet.retweet() 
            print('Retweeted the tweet!') 

            if LIKE: 
                tweet.favorite() 
                print('Liked the tweet!') 

            if FOLLOW: 
                if not tweet.user.following: 
                    tweet.user.follow() 
                    print('Followed the user!') 

            sleep(SLEEP_TIME) 

        except tweepy.TweepError as e: 
            print(e.reason) 

        except StopIteration: 
            break


print("Twitter bot which retweets, like tweets and follow users") 
print("Bot Settings") 
print("Like Tweets :", LIKE) 
print("Follow users :", FOLLOW) 

main()
