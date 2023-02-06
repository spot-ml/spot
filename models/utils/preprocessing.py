'''
This python util file is meant for basic pre-processing of text before converting it into vector embeddings in different ML models.
'''

import nltk
import re
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def clean_text(text):
    """Removes HTML tags and removes punctuation from the text"""
    text = text.lower() 
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'www\S+', '', text) 
    text = re.sub(r'<.*?>', '', text)  
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub('\s+', ' ', text) 
    return text

def remove_stopword(text, stop_words):
    """Removes common stopwords such as "the" and "a" from the text""" 
    return " ".join([word for word in text.split() if word not in (stop_words)])

def lemma_text(text, lemmatizer):
    """Reduces words to their base forms using lemmatization"""
    lemmatized_words = [lemmatizer.lemmatize(word) for word in tokenize(text)]
    return " ".join(lemmatized_words)

def tokenize(text):
    """Splits the text into individual words"""
    return text.split()

def process_text(text, model=1, lemmatizer=WordNetLemmatizer(), stop_words=stopwords.words('english')):
    """Main function to call above functions and return pre-processed text"""
    text = clean_text(text)
    text = remove_stopword(text, stop_words)
    if model==1:
      text = lemma_text(text, lemmatizer)
    return text