import pandas as pd
from germansentiment import SentimentModel

sentiment_model = SentimentModel()


def sentiment_on_texts(articles_df):
    length = len(articles_df)
    sentiments = []
    for index, row in articles_df.iterrows():
        print(f"\rRunning sentiment analysis on article {index + 1} of {length}", end="")
        text_class, text_probabilities = sentiment_model.predict_sentiment([row["text"]], output_probabilities=True)
        sentiments.append((text_class, text_probabilities))
    return sentiments


def main():
    articles_data = pd.read_csv("2-3-data-extended-keywords.csv")
    articles = pd.DataFrame(articles_data)

    headlines = articles["headline"]
    headlines_classes, headlines_probabilities = sentiment_model.predict_sentiment(headlines, output_probabilities=True)

    articles = articles.assign(sentiment_headline=headlines_classes)
    articles = articles.assign(sentiment_prob_headline=headlines_probabilities)

    text_sentiments = sentiment_on_texts(articles)
    texts_classes = [x[0][0] for x in text_sentiments]
    texts_probabilities = [x[1][0] for x in text_sentiments]
    articles["sentiment_text"] = texts_classes
    articles["sentiment_prob_text"] = texts_probabilities
    articles["sentiment_prob_headline_positive"] = articles.apply(
        lambda row: row["sentiment_prob_headline"][0][1], axis=1
    )
    articles["sentiment_prob_headline_negative"] = articles.apply(
        lambda row: row["sentiment_prob_headline"][1][1], axis=1
    )
    articles["sentiment_prob_headline_neutral"] = articles.apply(
        lambda row: row["sentiment_prob_headline"][2][1], axis=1
    )
    articles["sentiment_prob_text_positive"] = articles.apply(lambda row: row["sentiment_prob_text"][0][1], axis=1)
    articles["sentiment_prob_text_negative"] = articles.apply(lambda row: row["sentiment_prob_text"][1][1], axis=1)
    articles["sentiment_prob_text_neutral"] = articles.apply(lambda row: row["sentiment_prob_text"][2][1], axis=1)
    articles = articles.drop("sentiment_prob_headline", axis=1)
    articles = articles.drop("sentiment_prob_text", axis=1)
    articles.to_csv("3-4-data-extended-keywords-sentiment.csv", sep=",", encoding="utf-8", index=False)


if __name__ == "__main__":
    main()
