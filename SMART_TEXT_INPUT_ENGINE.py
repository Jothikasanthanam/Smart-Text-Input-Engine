
import re
import nltk

from textblob import TextBlob
from nltk.corpus import wordnet
from nltk.util import ngrams
from collections import defaultdict, Counter


training_sentences = [

    "I am going to school",
    "I am going to office",
    "I am going to market",
    "I am going to home",
    "I am going to college",
    "I am going to hospital",
    "I am going to temple",
    "I am going to park",

    "He is playing cricket",
    "She is reading a book",
    "They are going home",
    "We are watching movie",

    "Python is easy to learn",
    "I love learning python",

    "He goes to school daily",
    "She goes to office daily"
]

bigram_model = defaultdict(list)

for sentence in training_sentences:

    tokens = sentence.lower().split()

    for word1, word2 in ngrams(tokens, 2):

        bigram_model[word1].append(word2)


def clean_text(text):

    text = re.sub(r'[^A-Za-z\s]', '', text)

    return text


def spell_correct(sentence):

    words = sentence.split()

    corrected_words = []

    corrections = {}

    for word in words:

        corrected_word = str(TextBlob(word).correct())

        corrected_words.append(corrected_word)

        if word.lower() != corrected_word.lower():

            corrections[word] = corrected_word

    corrected_sentence = " ".join(corrected_words)

    return corrected_sentence, corrections



def grammar_correct(sentence):

    corrected = str(TextBlob(sentence).correct())

    return corrected


def predict_next_words(sentence, num_predictions=3):

    words = sentence.lower().split()

    if not words:
        return []

    last_word = words[-1]

    possible_words = bigram_model.get(last_word, [])

    if not possible_words:
        return ["No suggestions available"]

    word_counts = Counter(possible_words)

    predictions = []

    for word, count in word_counts.most_common(num_predictions):

        predictions.append(word)

    return predictions


def get_word_details(word):

    synsets = wordnet.synsets(word)

    if not synsets:

        return "Meaning not found", []

    meaning = synsets[0].definition()

    synonyms = set()

    for lemma in synsets[0].lemmas():

        synonyms.add(lemma.name())

    return meaning, list(synonyms)


def main():

  
    print(" SMART TEXT INPUT ENGINE ")

    user_input = input("\nEnter a sentence: ")


    cleaned_input = clean_text(user_input)


    corrected_sentence, corrections = spell_correct(cleaned_input)
    

    final_sentence = grammar_correct(corrected_sentence)

    print(" CORRECTED SENTENCE ")
    print("_____________________\n")

    print(final_sentence)



    print(" SPELL CORRECTIONS ")
    print("__________________________\n")

    if corrections:

        for wrong_word, correct_word in corrections.items():

            print(f"{wrong_word}  -->  {correct_word}")

    else:

        print("No spelling mistakes found")


    predictions = predict_next_words(final_sentence)

    print(" NEXT WORD SUGGESTIONS ")
    print("___________________________\n")

    for word in predictions:

        print(word)


    print(" DICTIONARY SUPPORT ")
    print("________________________")

    words = final_sentence.split()

    unique_words = set(words)


    stop_words = {

        "i", "am", "is", "are",
        "was", "were", "to",
        "the", "a", "an",
        "of", "and", "in",
        "on", "at"
    }

    for word in unique_words:

        
        if word.lower() in stop_words:
            continue

        meaning, synonyms = get_word_details(word)

        print(f"\nWORD: {word}")

        print("Meaning:")
        print(meaning)

        print("Synonyms:")

        if synonyms:

            print(", ".join(synonyms[:5]))

        else:

            print("No synonyms found")


if __name__ == "__main__":

    main()
