# deleteTweet

This is a tool used to delete past Tweets, Likes, and DMs. 

You will have to create an API key from https://apps.twitter.com/ with Direct Messages permisions
if that is a feature you want to use.

You will need to perminantly turn off DebugMode or specify in the CLI options. 

Usage:

python deleteTweet.py [Options]
"-t", "--tweets", help="Delete the Tweets", action='store_true'
"-l", "--likes", help="Delete your likes", action='store_true'
"-d", "--DM", help="Delete da DMs", action='store_true'
"-k", "--keep", help="How many days to keep. Default 2", default=2
"-b" "--debug", help="Turn off debug mode", action='store_false'
