import twitter
twitter_search = twitter.twitter(domain="search.twitter.com")
trends = twitter_search.trends()
[ trend['name'] for trend in trends['trends'] ]