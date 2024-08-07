import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

articles_data = pd.read_csv('2-4-data-extended-keywords-sentiment.csv')
articles = pd.DataFrame(articles_data)

def create_line_chart_for_uploads_per_hour(articles):
    uploads_per_hour = articles['upload-hour'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    plt.plot(uploads_per_hour.index, uploads_per_hour.values, marker='o', linestyle='-', color='b')
    plt.title('Uploads per hour')
    plt.xlabel('Hour of day')
    plt.ylabel('Uploads')
    plt.xticks(range(24))
    plt.grid(True)
    plt.show()
create_line_chart_for_uploads_per_hour(articles)


def create_line_chart_for_uploads_per_weekday(articles):
    uploads_per_weekday = articles['weekday'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], fill_value=0)
    plt.figure(figsize=(12, 6))
    plt.plot(uploads_per_weekday.index, uploads_per_weekday.values, marker='o', linestyle='-', color='b')
    plt.title('Anzahl der Uploads pro Wochentag')
    plt.xlabel('Wochentag')
    plt.ylabel('Anzahl der Uploads')
    plt.grid(True)
    plt.show()
create_line_chart_for_uploads_per_weekday(articles)


def create_heatmap_of_hour_per_weekday(articles):
    heatmap_data = articles.groupby(['weekday', 'upload-hour'], observed=False).size().unstack(fill_value=0).reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ], fill_value=0)
    plt.figure(figsize=(12, 5))
    sns.heatmap(heatmap_data, annot=True, fmt='d', cbar=False, rasterized=True, cmap="crest")
    plt.title('Uploads per weekday and hour')
    plt.xlabel('Hour')
    plt.ylabel('Weekday')
    plt.show()
create_heatmap_of_hour_per_weekday(articles)

def create_bar_chart_for_median_by_hour_and_by_weekday(articles):
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    articles['weekday'] = pd.Categorical(articles['weekday'], categories=weekday_order, ordered=True)
    median_by_hour = articles.groupby('upload-hour')['length'].median()
    median_by_weekday = articles.groupby('weekday', observed=False)['length'].median()
    median_by_weekday_hour = articles.groupby(['weekday', 'upload-hour'], observed=False)['length'].median().unstack()
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    axs[0].bar(median_by_hour.index, median_by_hour.values)
    axs[0].set_title('Median length by hour of upload')
    axs[0].set_xlabel('Upload hour')
    axs[0].set_ylabel('Median length')
    axs[1].bar(median_by_weekday.index, median_by_weekday.values)
    axs[1].set_title('Median length by weekday')
    axs[1].set_xlabel('Weekday')
    axs[1].set_ylabel('Median length')
    axs[1].set_xticks(range(len(weekday_order)))
    axs[1].set_xticklabels(weekday_order)
    plt.tight_layout()
    plt.show()
create_bar_chart_for_median_by_hour_and_by_weekday(articles)

def create_heatmap_of_article_length_by_hour_and_weekday(articles):
    median_data = articles.groupby(['upload-hour', 'weekday'], observed=False)['length'].median().reset_index()
    pivot_data = median_data.pivot_table(index='weekday', columns='upload-hour', values='length', aggfunc='median', observed=False)
    plt.figure(figsize=(22, 10))
    sns.heatmap(pivot_data, annot=True, rasterized=True, cmap="crest", fmt='.1f')
    plt.title('Median of length after upload hour and weekday')
    plt.xlabel('Hour')
    plt.ylabel('Weekday')
    plt.show()
create_heatmap_of_article_length_by_hour_and_weekday(articles)

def create_heatmap_plots_for_hours_per_category(articles):
    upload_counts = articles.groupby(['category', 'upload-hour']).size().unstack(fill_value=0)
    for category in upload_counts.index:
        plt.figure(figsize=(24, 1))
        sns.heatmap(upload_counts.loc[[category]], annot=True, fmt='d', cbar=False, rasterized=True, cmap="crest")
        plt.title(f'Uploads per hour for category: {category}')
        plt.xlabel('hour')
        plt.yticks([])
        plt.show()
create_heatmap_plots_for_hours_per_category(articles)

def create_heatmap_plots_for_articles_per_hour_unified(articles):
    heatmap_data = articles.groupby(['category', 'upload-hour']).size().unstack(fill_value=0)
    scaled_heatmap_data = heatmap_data.div(heatmap_data.sum(axis=1), axis=0) * 100
    plt.figure(figsize=(10, 6))
    sns.heatmap(scaled_heatmap_data, annot=False, cbar=False, rasterized=True, cmap="crest")
    plt.title('Uploads by category and hour')
    plt.xlabel('Hour')
    plt.ylabel('Category')
    plt.show()
create_heatmap_plots_for_articles_per_hour_unified(articles)

def create_bar_plots_for_articles_per_weekday(articles):
    upload_weekday_counts = articles.groupby(['category', 'weekday'], observed=False).size().unstack(fill_value=0)
    upload_weekday_counts = upload_weekday_counts.reindex(columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    for category in upload_weekday_counts.index:
        plt.figure(figsize=(10, 2))
        sns.barplot(x=upload_weekday_counts.columns, y=upload_weekday_counts.loc[category].values)
        plt.title(f'Upload behavior category: {category}')
        plt.xlabel('Wochentag')
        plt.ylabel('Anzahl der Artikel')
        plt.xticks(rotation=45)
        plt.show()
create_bar_plots_for_articles_per_weekday(articles)

def create_heatmap_plots_for_articles_per_weekday_unified(articles):
    heatmap_data = articles.groupby(['category', 'weekday'], observed=False).size().unstack(fill_value=0)
    scaled_heatmap_data = heatmap_data.div(heatmap_data.sum(axis=1), axis=0) * 100
    plt.figure(figsize=(10, 6))
    sns.heatmap(scaled_heatmap_data, annot=False, cbar=False, rasterized=True, cmap="crest")
    plt.title('Uploads per category and hour')
    plt.xlabel('Weekday')
    plt.ylabel('Category')
    plt.show()
create_heatmap_plots_for_articles_per_weekday_unified(articles)

def create_heatmap_plots_for_articles_per_hour_per_weekday(articles):
    categories = articles['category'].unique()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    hours = np.arange(0, 24)
    index = pd.MultiIndex.from_product([categories, weekdays, hours], names=['Category', 'Weekday', 'Hour'])
    upload_category_weekday_hour_counts = articles.groupby(['category', 'weekday', 'upload-hour'], observed=False).size().reindex(index, fill_value=0).unstack(level='Hour')
    upload_category_weekday_hour_counts = upload_category_weekday_hour_counts.reindex(weekdays, level='Weekday')
    for category in categories:
        plt.figure(figsize=(14, 4))
        sns.heatmap(upload_category_weekday_hour_counts.loc[category], annot=True, fmt='d', cbar=False, rasterized=True, cmap="crest")
        plt.title(f'Upload behavior for category: {category}')
        plt.xlabel('hour of day')
        plt.ylabel('weekday')
        plt.show()
create_heatmap_plots_for_articles_per_hour_per_weekday(articles)

def create_bar_chart_for_length_per_category(articles):
    median_by_category = articles.groupby('category')['length'].median().reset_index()
    plt.figure(figsize=(18, 6))
    sns.barplot(x='category', y='length', data=median_by_category)
    plt.title('Median length of category')
    plt.xlabel('Category')
    plt.ylabel('Median')
    plt.show()
create_bar_chart_for_length_per_category(articles)

def create_heatmap_for_length_per_category_by_hour_and_weekday(articles):
    categories = articles['category'].unique()
    for category in categories:
        category_data = articles[articles['category'] == category]
        median_data = category_data.groupby(['upload-hour', 'weekday'], observed=False)['length'].median().reset_index()
        pivot_data = median_data.pivot_table(index='weekday', columns='upload-hour', values='length', aggfunc='median', observed=False)
        plt.figure(figsize=(23, 5))
        sns.heatmap(pivot_data, annot=True, rasterized=True, cmap="crest", fmt='.0f')
        plt.title(f'Median of length for category "{category}" by upload hour and weekday')
        plt.xlabel('Hour')
        plt.ylabel('Weekday')
        plt.show()
create_heatmap_for_length_per_category_by_hour_and_weekday(articles)

def create_bar_charts_for_length_of_hour_per_weekday_per_category(articles):
    categories = articles['category'].unique()
    for category in categories:
        category_data = articles[articles['category'] == category]
        median_by_hour = category_data.groupby('upload-hour', observed=False)['length'].median().reset_index()
        plt.figure(figsize=(10, 4))
        sns.barplot(x='upload-hour', y='length', data=median_by_hour)
        plt.title(f'Median of length per hour and category {category}')
        plt.xlabel('upload hour')
        plt.ylabel('Median of length')
        plt.xticks(rotation=45)
        plt.show()
create_bar_charts_for_length_of_hour_per_weekday_per_category(articles)
