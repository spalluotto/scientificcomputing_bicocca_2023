import re
import matplotlib.pyplot as plt

def plot_freq(filename):
    """Reads a file, counts word frequencies, and plots the most frequent words."""
    word_count = {}
    with open(filename, 'r') as f:
        for line in f:
            words = re.findall(r'\b\w+\b', line.lower())
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    sorted_words = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    # top 25
    freq_words = list(sorted_words.keys())[:25]
    word_fr = [sorted_words[word] for word in freq_words]

    # Plot
    plt.figure()
    plt.barh(freq_words, word_fr, color='orange')
    plt.xlabel('Frequency')
    plt.ylabel('Word')
    plt.gca().invert_yaxis()
    plt.show()
