import string
from collections import defaultdict
from math import log

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

def build_vocabulary(dataset):
    vocabulary = set()
    for text, _ in dataset:
        words = preprocess_text(text)
        vocabulary.update(words)
    return list(vocabulary)

def calculate_probabilities(dataset, vocabulary):
    class_counts = defaultdict(int)
    word_counts = defaultdict(lambda: defaultdict(int))
    total_docs = len(dataset)

    for text, label in dataset:
        class_counts[label] += 1
        words = preprocess_text(text)
        for word in words:
            if word in vocabulary:
                word_counts[label][word] += 1

    prior_probs = {label: class_counts[label] / total_docs for label in class_counts}

    word_likelihoods = {}
    for label in class_counts:
        total_words_in_class = sum(word_counts[label].values())
        word_likelihoods[label] = {
            word: (word_counts[label][word] + 1) / (total_words_in_class + len(vocabulary))
            for word in vocabulary
        }

    return prior_probs, word_likelihoods

def naive_bayes_classifier(text, prior_probs, word_likelihoods, vocabulary):
    words = preprocess_text(text)
    class_scores = {}

    for label in prior_probs:
        class_scores[label] = log(prior_probs[label])
        for word in words:
            if word in vocabulary:
                class_scores[label] += log(word_likelihoods[label].get(word, 1 / len(vocabulary)))

    return max(class_scores, key=class_scores.get)

def evaluate_classifier(test_data, prior_probs, word_likelihoods, vocabulary):
    correct = 0
    for text, label in test_data:
        predicted_label = naive_bayes_classifier(text, prior_probs, word_likelihoods, vocabulary)
        if predicted_label == label:
            correct += 1
    return correct / len(test_data)

dataset = [
    ("I love this movie", 1),
    ("This film is fantastic", 1),
    ("What an amazing experience", 1),
    ("I dislike this movie", 0),
    ("Not a great film", 0),
    ("This is terrible", 0)
]

training_data = dataset[:4]
test_data = dataset[4:]

vocabulary = build_vocabulary(training_data)
prior_probs, word_likelihoods = calculate_probabilities(training_data, vocabulary)
accuracy = evaluate_classifier(test_data, prior_probs, word_likelihoods, vocabulary)

print(f"Vocabulary: {vocabulary}")
print(f"Prior probabilities: {prior_probs}")
print(f"Word likelihoods: {word_likelihoods}")
print(f"Accuracy: {accuracy:.2f}")