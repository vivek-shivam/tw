
import tweepy
from paralleldots import set_api_key,get_api_key
from paralleldots import *
import nltk
from nltk.corpus import *
from collections import Counter

consumer_key=""
consumer_secret=""
access_token=""
access_secret=""

nltk.download('stopwords')
stop_word=list(stopwords.words('english'))
stop_words=[]
for word in stop_word:
    stop_words.append(word.upper())
stop_words.extend(stop_word)
set_api_key("**IOEJcuuQyQwF0R1Ii7BbZO3jadNBpjVPsdaZLYdNJo4")#remove *
get_api_key()
oauth = tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
def menu():
    print('''1:-Retrieve Tweets
    2:-Count the followers
    3:-Determine the sentiment
    4:-Determine location,language and time zone.
    5:-Compare tweets 
    6:-Analyze top usage 
    7:-Tweet a message
    8:-Update status
    9:-exit 
    ''')
    choice = int(input('enter your choices'))
    if (choice == 1):
        tweets()
        menu()
    elif (choice == 2):
        count()
        menu()
    elif (choice == 3):
        sentimentl()
        menu()
    elif (choice == 4):
        location()
        menu()
    elif (choice == 5):
        compare()
        menu()
    elif (choice == 6):
        top_usage()
        menu()
    elif (choice == 7):
        update_status()
        menu()
    elif (choice == 8):
        exit()
    else:
        print('invalid choice')


def tweets():
    q=input("enter what you want : ")
    search_results = api.search(q)
    for search_result in search_results:
        print(search_result.text)
def count():
    user_name=input("enter username")
    user = api.get_user('@'+user_name)
    print(user.screen_name)
    print(user.followers_count)
def sentimentl():
    print("sentiments")
    tweets = api.search(input("with hash:"))
    for tweet in tweets:
        print(sentiment(tweet.text)["sentiment"])



def location():
    q = input("enter what you want : ")
    search_results = api.search(q)
    for search_result in search_results:
        print('location = ',search_result.user.location)
        print('language = ',search_result.user.lang)
        print('time_zone = ',search_result.user.time_zone)
def compare():
    a = input('first user: ')
    b = input('second user: ')
    c = input('words used by first user: ')
    d = input('words used by second user: ')
    tw1 = api.user_timeline(screen_name=a)
    tw2 = api.user_timeline(screen_name=b)
    s1=''
    s2=''
    for tweet in tw1:
        s1+=tweet.text
    print(s1.count(c))
    for tweet in tw2:
        s2+=tweet.text
    print(s1.count(d))
def top_usage():
    tweets=api.user_timeline(input("enter a user : "))
    word=[]
    for tweet in tweets:
        text=tweet.text
        list1=text.split()
        # print(list1)
        for words in list1:
            if words not in stop_words:
                word.append(words)
    count1=Counter(word).most_common(4)
    print(count1)

def update_status():
    msg=input()
    api.update_status(msg)
menu()