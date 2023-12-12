import newspaper

URL = "https://www.bloomberg.co.jp/"

website = newspaper.build(URL)

for article in website.articles:
    article.download()
    article.parse()
    article.nlp()
    print(article.title)
    print(article.url)