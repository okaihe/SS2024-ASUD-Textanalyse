import pandas as pd
import nltk
import matplotlib.pyplot as plt
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

articles_data = pd.read_csv('2-4-data-extended-keywords-sentiment.csv')
articles = pd.DataFrame(articles_data)
articles.head()

# Bevor Texte mit Algorithmen wie `BERTopic` analysiert werden, sollten sie
# vorverarbeitet werden. Dazu zaehlt beispielsweise das Entfernen von
# Stoppwoertern, da diese ansonsten eventuell eigene Kategorien erhalten
# koennen. Dafuer wird die Bibliothek `nltk` verwendet, die entsprechende
# Datensaetze zur Verfuegung stellt. Ausserdem werden Woerter auf ihren
# Wortstamm reduziert, was die Textmenge reduziert und dabei hilft gleiche
# Woerter unabhaengig ihrer Konjunktion auch als solche zu erkennen.
stemmer = SnowballStemmer('german')
stop_words = set(stopwords.words('german'))

def preprocess_text_nltk(text):
    text = text.lower()
    tokens = word_tokenize(text, language='german')
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

articles['processed_text'] = articles['text'].apply(preprocess_text_nltk)
articles.head()

# Nun kann das Topic Modeling mit `BERTopic` durchgefuehrt werden. Dazu wird ein
# neues `topic_model` erstellt und diesem ueber die `fit_transform`-Funktion die
# Dokumente bzw. die Artikeltexte uebergeben. Fuer jeden Artikel wird
# anschliessend im DataFrame die von Bertopic ermittelte Kategorie angefuegt. 
documents = articles['processed_text'].tolist()
topic_model = BERTopic(language="multilingual")
topics, probs = topic_model.fit_transform(documents)
articles['topic'] = topics
articles.head()

# Zur Veranschaulich der Verteilung der Themen wird eine Funktion definiert:
def visualize_topic_distribution(articles, topic_column_name):
    topic_counts = articles[topic_column_name].value_counts()
    plt.figure(figsize=(30, 6))
    topic_counts.plot(kind='bar', color='skyblue')
    plt.xlabel('Topic')
    plt.ylabel('Count of articles')
    plt.title('Distribution of topics')
    plt.xticks(ticks=range(len(topic_counts)), labels=[f'{i}' for i in topic_counts.index], rotation=45)
    plt.show()

# Der nachfolgende Graph zeigt die Verteilung der Topics. Wie man sehen kann,
# faellt ein Grossteil der Artikel, ungefaehrt die Haelfe, unter die Kategorie
# `-1`. Dieser Kategorie ordnet `BERTopic` alle `Outlier` zu, also Ausreisser
# zu, die keiner Kategorie zugeordnet werden konnten.
visualize_topic_distribution(articles, "topic")

# Dieses Problem zeigt sich ebenfalls in der von `BERTopic` generierten
# Darstellung. Alle grauen Punkte stellen die Ausreisser dar.
topic_model.visualize_documents(documents, hide_document_hover=True, hide_annotations=True)

# Ein weiteres Problem stellt die Menge an gefunden Topics mit 100+
# verschiedenen Themen dar. Fuer beide Probleme bietet `BERTopic` jedoch
# Loesungen. Die Menge an Kategorien kann jedoch ueber entsprechende
# Funktionsargumente selbststaendig angepasst werden. Im Folgenden wird die
# Anzahl an Topics auf 70 gesetzt, um die Menge an Themen leicht einzugrenzen
# und Topics, die nur aeusserst selten auftreten nicht zu beruecksichtigen.
documents = articles['processed_text'].tolist()
topic_model = BERTopic(language="multilingual", nr_topics=70)
topics, probs = topic_model.fit_transform(documents)
articles['topic'] = topics
articles.head()

visualize_topic_distribution(articles, "topic")

topic_model.visualize_documents(documents, hide_document_hover=True, hide_annotations=True)

# Als naechstes sollen die Ausreisser noch eingegrenzt werden. `BERTopic` stellt
# dafuer mehrere Strategien zur Verfuegung. Hier verwendet wird die automatische
# Reduzierung durch `BERTopic` ueber die Funktion `topic_model.reduce_outliers(documents, topics)`.
# Diese werden in der neuen Spalte `new_topics` gespeichert.
articles['new_topic'] = topic_model.reduce_outliers(documents, topics)

visualize_topic_distribution(articles, "new_topic")
# Wie zu sehen ist, konnte eine Vielzahl an Ausreissern andern Topics zugeordnet
# werden. Die erweiterten Kategorien koennen ebenso im Cluster-Diagram angezeigt werden.
topic_model.visualize_documents(documents, hide_document_hover=True, hide_annotations=True)
# Auch diese Uebersicht stellt eine gute Visualisierung zu den Themenschwerpunkten von `n-tv` dar.
# Eine weitere von `BERTopic` zur Verfuegung gestellte Visualiserung stellt ebenfalls gut die Themen dar:
topic_model.visualize_topics()
