# importing the module
import tweepy
  
# personal details
consumer_key ="x4rkNPaNKiEDLSUkT2ApkLNH9"
consumer_secret ="jSRKgf8ZzvkdSXnTdgL0DcWzGzNoMhpvqWtb8S5gKoFLwXqvVF"
access_token ="1562847334999805953-fbWlqFcOk4oLoqHKXGGXlSjAyGm0NG"
access_token_secret ="VLYbBq1kuATM1cW19oWMjMSILLcKQ5uj5KKPx4QJ3J0U8"

#ORMmNWpFa8uS-vnuX_mYadxGL4wHt9dcVJksj8oSBYtVN40P_5  
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
  
# update the status
api.update_status(status ="Hello Everyone !")