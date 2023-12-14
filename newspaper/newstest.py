from newspaper import Article

URL = "https://diamond-rm.net/overseas/american_economy/472725/"
website = Article(URL, memoize_articles=False)

website.download()
website.parse()
print(website.publish_date)