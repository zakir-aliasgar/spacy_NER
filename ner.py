import spacy
from collections import defaultdict

list_languages = ['ca', "zh", "da", "nl", "fr", "de", "el", "it",
                  "ja", "lt", "mk", "xx", "nb", "pl", "pt", "ro", "ru", "es", ""]


def ner_spacy(text, lang):
    ner_list = []

    if lang == "en":
        nlp = spacy.load("en_core_web_sm")

        doc = nlp(text)

        for ent in doc.ents:
            ner_dict = defaultdict(str)
            ner_dict['text'] = ent.text
            ner_dict['type'] = ent.label_
            ner_dict['start_pos'] = ent.start_char
            ner_dict['end_pos'] = ent.end_char

            ner_list.append(ner_dict)
        return ner_list

    if lang in list_languages:
        model = lang + "_core_news_sm"
        nlp = spacy.load(model)

        doc = nlp(text)

        for ent in doc.ents:
            ner_dict = defaultdict(str)
            ner_dict['text'] = ent.text
            ner_dict['type'] = ent.label_
            ner_dict['start_pos'] = ent.start_char
            ner_dict['end_pos'] = ent.end_char

            ner_list.append(ner_dict)
        return ner_list


text = input("Please enter text:")
language = input("Please enter language:")

entity_list = ner_spacy(text, language)
