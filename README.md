# Smart Text Input Engine

## Project Overview
Smart Text Input Engine is a Python NLP project that performs:
- Spell Correction
- Grammar Correction
- Next Word Prediction
- Dictionary Meaning and Synonyms

The system improves text input using NLP techniques.

---

## Features

### Spell Correction
Corrects misspelled words.

Example:
recieve → receive

### Grammar Correction
Fixes simple grammar mistakes.

Example:
he go to school → he goes to school

### Next Word Prediction
Suggests likely next words using N-grams.

Example:
I am going to → school / office / market

### Dictionary Support
Displays:
- Meaning
- Synonyms

---

## Technologies Used

- Python
- NLTK
- TextBlob
- WordNet
- N-grams

---

## Install Required Packages

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

---

## Example Input

I am gonig to schol

## Example Output

I am going to school

Suggestions:
- school
- office
- market

---

## NLP Concepts Used

- Tokenization
- Corpus
- N-grams
- Spell Correction
- Grammar Correction
- Stop Words
- Dictionary Processing