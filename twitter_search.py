import json
from requests_oauthlib import OAuth1Session

consumer_key = 'm8fmmQGoGbRpooxPGwgGg'
consumer_secret = 'Llbr5TBIL0VcxZNS4jcIGXOq3qelCADnthYfjUeUQs'
access_token = '312682302-uvj5vhZYfgCYt75opEA7gnfDz7eaOvcNUUL3UgbL'
access_token_secret = 'jPwIHW2tjE3GQVgbL3JHXzosOBcTKsUpFsWdjfMFyU8EI'

twitter = OAuth1Session(consumer_key, consumer_secret,
                        access_token, access_token_secret)

url = 'https://api.twitter.com/1.1/search/tweets.json'

search_word = input('検索ワードを入力 >> ')
params = {'count': 100, 'q': search_word, 'lang': 'ja'}

res = twitter.get(url, params=params)

if res.status_code == 200:
    tweet_list = json.loads(res.text)
    for tweet in tweet_list['statuses']:
        print(tweet['user']['name'], '(@', tweet['user']
              ['screen_name'], ') : \n', tweet['text'])
        print('-*-*-*--*-*-*--*-*-*--*-*-*--*-*-*-')
