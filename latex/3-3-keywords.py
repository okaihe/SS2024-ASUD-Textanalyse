import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

articles_data = pd.read_csv('2-4-data-extended-keywords-sentiment.csv')
articles = pd.DataFrame(articles_data)
articles.head()

keywords_df = articles['keywords'].str.split(',', expand=True)
keywords_df = keywords_df.apply(lambda x: x.str.strip())
keywords_df.head()

invalid_rows = keywords_df[keywords_df[10].notna()]

keywords_df = keywords_df.iloc[:, :10]
keywords_df.head()

G = nx.Graph()

def create_graphml_file_for_gephi(filename: str):
    word_count = {}
    for index, row in keywords_df.iterrows():
        words = row.dropna().values
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
    for index, row in keywords_df.iterrows():
        words = row.dropna().values
        for i, word1 in enumerate(words):
            if word_count[word1] > 10:
                for j in range(i + 1, len(words)):
                    word2 = words[j]
                    if word1 != word2 and word_count[word2] > 10:
                        edge = tuple(sorted([word1, word2]))
                        if not G.has_edge(word1, word2):
                            G.add_edge(word1, word2, weight=1)
                        else:
                            G.edges[edge]['weight'] += 1
    nodes_to_remove = [node for node in G.nodes if word_count[node] <= 10]
    G.remove_nodes_from(nodes_to_remove)
    nx.write_graphml(G, f"{filename}")

create_graphml_file_for_gephi("ntv-topic-graph.graphml")
