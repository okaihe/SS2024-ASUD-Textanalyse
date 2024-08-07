import pandas as pd
from openai import OpenAI


def create_keywords_for_articles(openai_client, articles_df, start=0, end=5):
    print()
    for i in range(start, end):
        article_text = articles_df.iloc[i]["text"]
        completion = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Du fasst Nachrichtenartikel des Nachrichtensenders NTV anhand von Stichpunkten zusammenzufassen. Du gibst ausschliesslich die Stichwoerter durch Kommata getrennt zurueck. Die Stichwoerter sollen den Inhalt mit uebergeordneten Kategorien wie Politik, Wirtschaft, Gesellschaft, Auto, Sport, Unterhaltung und dergleichen beschreiben. Es sollen exakt 10 Stichwoerter generiert werden.",
                },
                {
                    "role": "user",
                    "content": article_text,
                },
            ],
        )
        keywords = completion.choices[0].message.content
        articles_df.at[i, "keywords"] = keywords
        print("\r", end="")
        print(f"Generated Keywords for {i + 1} articles", end="")
    return articles_df


def main():
    openai_client = OpenAI()
    articles_data = pd.read_csv("2-2-data-extended.csv")
    articles = pd.DataFrame(articles_data)
    articles["keywords"] = None
    articles = create_keywords_for_articles(openai_client, articles, 0, 10678)
    articles.to_csv("2-3-data-extended-keywords.csv", index=False)


if __name__ == "__main__":
    main()
