from newspaper import Article
import newspaper

URL = "https://diamond-rm.net/overseas/american_economy/472725/"
URL2 = "https://www.itmedia.co.jp/"
URL3 = "https://thebridge.jp/"
# website = Article(URL, memoize_articles=False)

# website.download()
# website.parse()
# print(website.publish_date)
# print(website.authors)
# print(website.text.replace("\n", ""))

website = newspaper.build(URL2, memoize_articles=False)
website2 = newspaper.build(URL3, memoize_articles=False)


i = 0
for article1 in website.articles:
    article1.download()
    article1.parse()
    article1.nlp()
    print("Index: ", i)
    print("Date: ", article1.publish_date)
    print("URL: ", article1.url)
    print("Author: ", article1.authors)
    print("Article: ", article1.text)

    if i > 9:
        break
    i += 1