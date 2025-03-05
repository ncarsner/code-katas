import json
from collections import Counter


def count_words_in_document(document, n):
    normalized_content = "".join(c.lower() if c.isalpha() else " " for c in document)
    word_frequencies = Counter(
        word for word in normalized_content.split() if word not in common_words
    )
    return word_frequencies.most_common(n)


document_file = "data/raw/speech_day_of_infamy.txt"
common_words = {
    "a", "about", "above", "after", "again", "against", "ain", "all", "am", "an", "and", "any", "are",
    "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but",
    "by", "can", "couldn", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have",
    "haven't", "having", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if",
    "in", "into", "is", "isn't", "it", "it's", "its", "itself", "just", "ll", "me", "mightn't", "more", "most",
    "mustn", "mustn't", "my", "myself", "needn", "needn't", "no", "nor", "not", "now", "of", "off", "on",
    "once", "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "same", "shan", "shan't",
    "she", "she's", "should", "should've", "shouldn", "shouldn't", "so", "some", "such", "than", "that",
    "that'll", "the", "their", "theirs", "them", "themselves", "then", "there", "these", "they", "this",
    "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "were", "weren't",
    "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "won", "won't", "wouldn",
    "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"
}


with open(document_file, "r") as file:
    doc_content = file.read()

n = 15  # Set this to however many common words you want
results = count_words_in_document(doc_content, n)

# print(json.dumps(result, indent=4))

for result in results:
    print(f"{result[1]} -- {result[0]}")
