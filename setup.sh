#!/bin/bash

python --version

# you must be using python 3.7.9
pip install -r requirements.txt
python -m spacy download en

# In site-packages/errant/__init__.py update line 11 -> 16 with the bellow
    # supported = {"en": "en_core_web_sm"}
    # if lang not in supported:
    #     raise Exception("%s is an unsupported or unknown language" % lang)

    # # Load spacy
    # nlp = nlp or spacy.load(supported[lang], disable=["ner"])
