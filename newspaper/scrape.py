from newspaper import Article

URL = "https://www.reuters.com/world/middle-east/hunger-rises-gaza-un-prepares-vote-ceasefire-resolution-2023-12-12/"

article = Article(URL)
article.download()
article.parse()