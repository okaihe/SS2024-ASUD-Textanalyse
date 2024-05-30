import spacy
from spacy.lang.de.examples import sentences

nlp = spacy.load("de_core_news_sm")
ner_categories = ["PERSON", "ORG", "GPE", "PRODUCT"]

doc = nlp(sentences[0])
print(doc)

# for token in doc:
#     print(token.text, token.pos_, token.dep_)

print(doc.ents)

entities = []
for ent in doc.ents:
    if ent.label_ in ner_categories:
        entities.append((ent.text, ent.label_))

# for entity, category in entities:
#     print(f"{entity}: {category}")
