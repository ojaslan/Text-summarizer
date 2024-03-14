import tkinter as tk
from tkinter import scrolledtext
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest
import nltk

# Download NLTK stopwords data
nltk.download('stopwords')

def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    word_freq = {}
    sentences = sent_tokenize(text)

    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        for word in words:
            if word.isalnum() and word not in stop_words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
    return word_freq, sentences


def summarize_text():
    text = input_text.get("1.0", tk.END)
    word_freq, sentences = preprocess_text(text)

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += word_freq[word]
                else:
                    sentence_scores[sentence] = word_freq[word]

    summary_sentences = nlargest(3, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, summary)


root = tk.Tk()
root.title("Text Summarizer")

input_text = scrolledtext.ScrolledText(root, width=50, height=20)
input_text.pack(pady=10)

summarize_button = tk.Button(root, text="Summarize Text", command=summarize_text)
summarize_button.pack(pady=5)

output_text = scrolledtext.ScrolledText(root, width=50, height=10)
output_text.pack(pady=10)

root.mainloop()
