import newspaper

URL = "https://diamond-rm.net/"
website = newspaper.build(URL, memoize_articles=False)

website.download()
website.parse()