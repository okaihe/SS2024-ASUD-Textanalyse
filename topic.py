from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired

from collectHeadlines import collect_article_contents_from

representation_model = KeyBERTInspired()
topic_model = BERTopic(language="multilingual", representation_model=representation_model)

articles = collect_article_contents_from("ntv-data")
headlines = [article["headline"] for article in articles]

topics, probs = topic_model.fit_transform(headlines)

print(topic_model.get_topic_info())
