import tweepy
import time

auth = tweepy.OAuthHandler('NcTpdBvjhLLUj4BQbAgmzb62Q',
                           'r8w1VaHzZ7GcwxaT9gmpyRAXww0BM0cXNOI1w16DAyGijPL9D5')
auth.set_access_token('1460322385413001221-ySuYGuYR6bSIaaub4bCvMKjI6n2OoQ',
                      'EApFJRLnX8AyhJBadbve3Qt5EujqAUt3AWMPwalZTtsfE')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = 'faustao'
numero = 30

for tweet in tweepy.Cursor(api.search, search).items(numero):
    try:
        print("nome do usuario: @" + tweet.user.screen_name)
        api.update_status("@" + tweet.user.screen_name + " Essa fera ai meu!", in_reply_to_status_id=tweet.id)
        print("tuite enviado corretamente")
        time.sleep(30)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break