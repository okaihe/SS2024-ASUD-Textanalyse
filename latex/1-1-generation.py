import csv
import os
import re
from datetime import datetime
from typing import Dict, List

from bs4 import BeautifulSoup


def get_content_of(article_path: str) -> str:
    result = ""
    with open(article_path, "r", encoding="utf-8") as article:
        result = article.read()
    if result != "":
        return result
    raise Exception("File not found")


def extract_text_from_html_article(html_text: str) -> str:
    soup = BeautifulSoup(html_text, "html.parser")
    article_text = soup.find("div", class_="article__text")
    if article_text:
        soup = BeautifulSoup(article_text.text, "html.parser")
        for aside in soup.find_all("div", class_="article__aside"):
            aside.decompose()
        output = soup.text.strip()
        output = re.sub(" +", " ", output)
        output = output.replace("\n", "")
        return output
    raise Exception("No article text was found")


def extract_exact_date_from_html_article(html_text: str) -> str | None:
    soup = BeautifulSoup(html_text, "html.parser")
    date = soup.find("span", class_="article__date")
    if date:
        output = date.get_text()
        return output
    print("No date was found")
    return None


def convert_filename_to_article_headline(article_filename: str) -> str:
    headline = (" ").join(article_filename.split("-")[:-1])
    return headline


def parse_ntv_datetime(date_string: str):
    try:
        datetime_obj = datetime.strptime(date_string, "%d.%m.%Y, %H:%M Uhr")
        date = datetime_obj.date()
        time = datetime_obj.time()
        return date, time
    except:
        return None, None


def collect_article_contents_from(path: str) -> List[Dict[str, str]]:
    collection = []
    dates = os.listdir(path)
    count_articles = 0
    print()
    for date in dates:
        categories = os.listdir(f"{path}/{date}")
        for category in categories:
            article_list = os.listdir(f"{path}/{date}/{category}")
            for article in article_list:
                if article != "rss.json" and article != ".ipynb_checkpoints":
                    count_articles += 1
                    print("\r", end="")
                    print(f"Scanned articles: {count_articles} - scanning: {article}", end="")
                    article_content = get_content_of(f"{path}/{date}/{category}/{article}")
                    article_text = extract_text_from_html_article(article_content)
                    article_extracted_date = extract_exact_date_from_html_article(article_content)
                    article_date, article_time = parse_ntv_datetime(article_extracted_date)
                    collection.append(
                        {
                            "date": article_date,
                            "time": article_time,
                            "category": category,
                            "headline": convert_filename_to_article_headline(article),
                            "filename": article,
                            "text": article_text,
                        }
                    )
    return collection


def main():
    content = collect_article_contents_from("ntv-data")
    with open("2-1-data.csv", "w", encoding="utf-8", newline="") as output_file:
        fc = csv.DictWriter(output_file, fieldnames=content[0].keys())
        fc.writeheader()
        fc.writerows(content)


if __name__ == "__main__":
    main()
