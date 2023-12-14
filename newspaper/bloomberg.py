import newspaper
import csv
import datetime

csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = "bloomberg_" + csv_date + ".csv"

f = open(csv_file_name, "w", encoding="utf-8", errors="ignore")
writer = csv.writer(f, lineterminator="\n")
csv_header = ["Article num", "Title", "URL", "Summary"]

writer.writerow(csv_header)

URL = "https://www.bloomberg.co.jp/"

website = newspaper.build(URL, memoize_articles=False)

i = 0
for article in website.articles:
    article.download()
    article.parse()
    article.nlp()
    print("Article:", str(i), ":", article.title)
    print(article.url)
    print(article.summary, end="\n\n")

    if i > 3:
        break
    i += 1