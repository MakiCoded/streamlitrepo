import nltk
import streamlit as st
import string

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


    #Load the text file and preprocess the data
with open('text.txt', 'r', encoding='utf-8') as f:

    data = f.read().replace('\n', ' ')

# Tokenize the text into sentences
sentences = sent_tokenize(data)

# Define a function to preprocess each sentence

def preprocess(sentence):

    # Tokenize the sentence into words

    words = word_tokenize(sentence)

    # Remove stopwords and punctuation

    words = [word.lower() for word in words if word.lower() not in stopwords.words('english') and word not in string.punctuation]

    # Lemmatize the words

    lemmatizer = WordNetLemmatizer()

    words = [lemmatizer.lemmatize(word) for word in words]

    return words

# Preprocess each sentences
preprocessed_sentences = [preprocess(sentence) for sentence in sentences] # type: ignore


# Define a function to find the most relevant sentence given a query

def get_most_relevant_sentence(query):

    # Preprocess the query

    query = preprocess(query)

    # Compute the similarity between the query and each sentence in the text

    max_similarity = 0

    most_relevant_sentence = ""

    for sentence in preprocessed_sentences:

        similarity = len(set(query).intersection(sentence)) / float(len(set(query).union(sentence)))

        if similarity > max_similarity:

            max_similarity = similarity

            most_relevant_sentence = " ".join(sentence)

    return most_relevant_sentence


def chatbot(question):

    # Get the most relevant sentence

    most_relevant_sentence = get_most_relevant_sentence(question)

    return most_relevant_sentence

st.title('Chatbot App')
query = st.text_input('Enter your question here:')

if query:

    answer = chatbot(query)

    st.write("Answer:", answer)

else:
    st.write("Please enter a question in the text box above.")
