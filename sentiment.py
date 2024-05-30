from germansentiment import SentimentModel
from collectHeadlines import collect_article_content_from

model = SentimentModel()

articles = collect_article_content_from("ntv-data")

headlines = [article["headline"] for article in articles]

classes = model.predict_sentiment(headlines)
print(classes)
