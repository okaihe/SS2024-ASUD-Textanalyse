import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

articles_data = pd.read_csv('2-4-data-extended-keywords-sentiment.csv')
articles = pd.DataFrame(articles_data)
articles.head()

def create_sentiment_result_plot(df, column):
    sentiment_count = []
    for sentiment_class, count in df[column].value_counts().items():
        sentiment_count.append( (sentiment_class, count) )
    labels, values = zip(*sentiment_count)
    plt.xlabel('Sentiment class')
    plt.ylabel('Count')
    plt.title(f'Sentiment analyse of {column}')
    plt.bar(labels, values)
    for i, value in enumerate(values):
        print(i, value)
        plt.text(i, value + 0.1, str(value), ha='center', va='bottom')
    plt.show()
create_sentiment_result_plot(articles, "sentiment_headline")

create_sentiment_result_plot(articles, "sentiment_text")

def create_category_result_plot(df, column, relative=False):
    categories = []
    category_count = []
    negatives = []
    neutrals = []
    positives = []
    for category, count in articles['category'].value_counts().items():
        negatives.append(articles[column][(articles.sentiment_text == 'negative') & (articles.category == category)].count())
        neutrals.append(articles[column][(articles.sentiment_text == 'neutral') & (articles.category == category)].count())
        positives.append(articles[column][(articles.sentiment_text == 'positive') & (articles.category == category)].count())
        categories.append(category)
    if relative:
        for i, category in enumerate(categories):
            count = articles[column][(articles.category == category)].count()
            negatives[i] = negatives[i] / count
            positives[i] = positives[i] / count
            neutrals[i] = neutrals[i] / count
    ind = np.arange(len(categories))
    fig, ax = plt.subplots()
    p1 = ax.bar(ind, positives, label='Positiv', color='seagreen')
    p2 = ax.bar(ind, neutrals, bottom=positives, label='Neutral', color='cornflowerblue')
    p3 = ax.bar(ind, negatives, bottom=[i+j for i,j in zip(positives, neutrals)], label='Negativ', color='lightcoral')
    ax.set_xlabel('Kategorien')
    ax.set_ylabel('Anteile')
    ax.set_xticks(ind)
    ax.set_xticklabels(categories)
    plt.xticks(rotation=90)
    ax.legend()
    plt.tight_layout()
    plt.show()
create_category_result_plot(articles, 'sentiment_headline', relative=True)

create_category_result_plot(articles, 'sentiment_text', relative = True)

def create_bar_chart_for_count_of_negative_articles_per_weekday(articles):
    negative_articles = articles[articles["sentiment_text"] == "negative"]
    negative_count_by_category = negative_articles.groupby("category").size()
    negative_count_by_category.plot(kind="bar", color="red", alpha=0.7)
    plt.title('Count of negative articles per category')
    plt.xlabel('category')
    plt.ylabel('count')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()
create_bar_chart_for_count_of_negative_articles_per_weekday(articles)

def create_bar_chart_for_percentage_of_negative_articles_per_weekday(articles):
    grouped = articles.groupby("weekday")["sentiment_text"].value_counts(normalize=True).unstack()
    grouped["negative_share"] = grouped["negative"] * 100
    grouped["negative_share"].plot(kind="bar", color="red", alpha=0.6)
    plt.title('Percentage of negative articles per weekday')
    plt.xlabel('weekday')
    plt.ylabel('percentage (%)')
    plt.xticks(rotation=45)
    plt.ylim(0, 100)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()
create_bar_chart_for_percentage_of_negative_articles_per_weekday(articles)

def create_bar_chart_for_percentage_of_neutral_articles_per_weekday(articles):
    grouped = articles.groupby("weekday")["sentiment_text"].value_counts(normalize=True).unstack()
    grouped["neutral_share"] = grouped["neutral"] * 100
    grouped["neutral_share"].plot(kind="bar", color="blue", alpha=0.6)
    plt.title('Percentage of neutral articles per weekday')
    plt.xlabel('weekday')
    plt.ylabel('percentage (%)')
    plt.xticks(rotation=45)
    plt.ylim(0, 100)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()
create_bar_chart_for_percentage_of_neutral_articles_per_weekday(articles)

def create_bar_chart_for_negative_articles_per_weekday_for_politics(articles):
    negative_politik_articles = articles[(articles["category"] == "politik") & (articles["sentiment_text"] == "negative")]
    negative_count_by_weekday = negative_politik_articles.groupby("weekday", observed=False).size()
    ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    negative_count_by_weekday = negative_count_by_weekday.reindex(ordered_days)
    negative_count_by_weekday.plot(kind="bar", color="red", alpha=0.6)
    plt.title('Anzahl der negativen Artikel pro Wochentag (Kategorie "politik")')
    plt.xlabel('Wochentag')
    plt.ylabel('Anzahl der negativen Artikel')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()
create_bar_chart_for_negative_articles_per_weekday_for_politics(articles)

def create_bar_chart_for_count_of_negative_articles_per_hour_of_politics(articles):
    negative_politik_articles = articles[(articles["category"] == "politik") & (articles["sentiment_text"] == "negative")]
    negative_count_by_hour = negative_politik_articles.groupby("upload-hour", observed=False).size()
    all_hours = range(24)
    negative_count_by_hour = negative_count_by_hour.reindex(all_hours, fill_value=0)
    negative_count_by_hour.plot(kind="bar", color="red", alpha=0.7)
    plt.title('Count of negative articles per hour of category "politik"')
    plt.xlabel('hour')
    plt.ylabel('count')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()
create_bar_chart_for_count_of_negative_articles_per_hour_of_politics(articles)

def create_bar_chart_for_relative_count_of_negative_articles_per_hour_of_politics(articles):
    politik_articles = articles[articles["category"] == "politik"]
    total_count_by_hour = politik_articles.groupby("upload-hour", observed=False).size()
    negative_count_by_hour = politik_articles[politik_articles["sentiment_text"] == "negative"].groupby("upload-hour").size()
    all_hours = range(24)
    total_count_by_hour = total_count_by_hour.reindex(all_hours, fill_value=0)
    negative_count_by_hour = negative_count_by_hour.reindex(all_hours, fill_value=0)
    negative_share_by_hour = (negative_count_by_hour / total_count_by_hour).fillna(0) * 100
    negative_share_by_hour.plot(kind="bar", color="red", alpha=0.6)
    plt.title('Anteil der negativen Artikel pro Stunde (Kategorie "politik")')
    plt.xlabel('Stunde')
    plt.ylabel('Anteil der negativen Artikel (%)')
    plt.xticks(rotation=0)
    plt.ylim(0, 100)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()
create_bar_chart_for_relative_count_of_negative_articles_per_hour_of_politics(articles)
