import pandas as pd


def main():
    articles_data = pd.read_csv("2-1-data.csv")
    articles = pd.DataFrame(articles_data)
    articles = articles.drop("filename", axis=1)
    articles.head()

    articles["upload"] = pd.to_datetime(articles["time"] + " " + articles["date"])
    articles = articles.dropna()
    articles.head()

    articles["upload-hour"] = articles["upload"].dt.hour
    articles["upload-hour"] = articles["upload-hour"].astype(int)
    articles.head()

    articles["weekday"] = articles["upload"].dt.dayofweek
    wochentag_map = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    articles["weekday"] = articles["weekday"].map(wochentag_map)
    articles.head()

    articles["length"] = articles["text"].apply(len)
    articles.head()

    articles.to_csv("2-2-data-extended.csv", index=False)


if __name__ == "__main__":
    main()
