from newspaper import Article
import nltk

URL = "https://www.reuters.com/world/middle-east/hunger-rises-gaza-un-prepares-vote-ceasefire-resolution-2023-12-12/"

article = Article(URL)
article.download()
article.parse()

print(article.publish_date)
print(article.authors)
print(article.text)
print(article.title)

# nltk.download("punkt")
article.nlp()
print(article.keywords)