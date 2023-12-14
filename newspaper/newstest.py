from newspaper import Article
import newspaper

URL = "https://diamond-rm.net/overseas/american_economy/472725/"
URL2 = "https://www.itmedia.co.jp/"
# website = Article(URL, memoize_articles=False)

# website.download()
# website.parse()
# print(website.publish_date)
# print(website.authors)
# print(website.text.replace("\n", ""))

website = newspaper.build(URL, memoize_articles=False)

i = 0
for article in website.articles:
    article.download()
    article.parse()
    article.nlp()
    print(article.publish_date)
    print(article.author)
    print(article.text)

    if i > 9:
        break
    i += 1