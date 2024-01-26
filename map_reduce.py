import json
from collections import Counter


def count_words_in_document(document, n):
    normalized_content = "".join(c.lower() if c.isalpha() else " " for c in document)
    word_frequencies = Counter(
        word for word in normalized_content.split() if word not in common_words
    )
    return word_frequencies.most_common(n)


document_file = r"C:\Users\Documents\speech_day_of_infamy.txt"
common_words = {
    "a", "about", "above", "after", "again", "against", "ain", "all", "am", "an", "and", "any", "are", # noqa
    "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", # noqa
    "by", "can", "couldn", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",  # noqa
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", # noqa
    "haven't", "having", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", # noqa
    "in", "into", "is", "isn't", "it", "it's", "its", "itself", "just", "ll", "me", "mightn't", "more", "most", # noqa
    "mustn", "mustn't", "my", "myself", "needn", "needn't", "no", "nor", "not", "now", "of", "off", "on", # noqa
    "once", "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "same", "shan", "shan't", # noqa
    "she", "she's", "should", "should've", "shouldn", "shouldn't", "so", "some", "such", "than", "that", # noqa
    "that'll", "the", "their", "theirs", "them", "themselves", "then", "there", "these", "they", "this", # noqa
    "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "were", "weren't", # noqa
    "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "won", "won't", "wouldn", # noqa
    "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" # noqa
}


with open(document_file, "r") as file:
    doc_content = file.read()

n = 15  # Set this to however many common words you want
results = count_words_in_document(doc_content, n)

# print(json.dumps(result, indent=4))

for result in results:
    print(f"{result[1]} -- {result[0]}")
