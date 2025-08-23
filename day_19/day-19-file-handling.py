# Day 19: File Handling
# Exercises: Level 1
# 1

from pathlib import Path

def readfunc(file):
    path = Path(file)
    content = path.read_text()

    lines = content.splitlines()
    words = content.split()

    print(f"Lines: {len(lines)}")
    print(f"words: {len(words)}")
    

readfunc('obama_speech.txt')
readfunc('michelle_obama_speech.txt')
readfunc('donald_speech.txt')

# 2
import json
from collections import Counter
def most_spoken_languages(file, n=10):
    path = Path(file)
    content = path.read_text(encoding="utf-8")
    countries = json.loads(content)

    languages = []
    for country in countries:
        languages.extend(country["languages"])

    lang_counter = Counter(languages)

    most_common = lang_counter.most_common(n)

    return most_common

top_lang = most_spoken_languages('countries_data.json')
for lang, count in top_lang:
    print(f"{lang}: {count} countries")


# 3
def most_populated_countries(file, n=10):
    path = Path(file)
    content = path.read_text(encoding="utf-8")
    countries = json.loads(content)

    country_population = [
        {"country": country["name"], "population": country["population"]} 
        for country in countries
    ]

    country_population.sort(key=lambda x: x["population"], reverse=True)

    return country_population[:n]

print(most_populated_countries('countries_data.json'))


# Exercises: Level 2
import re
emails = set()
with open('email_exchanges_big.txt', encoding="utf-8") as f:
    for line in f:
        matches = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", line)
        emails.update(matches)

emails = list(emails)
print(emails)

def find_most_common_words(text_or_file, n):
    try:
        with open(text_or_file, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        text = text_or_file
    
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    counter = Counter(words)

    return counter.most_common(n)

text = "Hello world, hello students. World is big, hello again!"
print(find_most_common_words(text, 3))

print(find_most_common_words('obama_speech.txt', 10))
print(find_most_common_words('michelle_obama_speech.txt', 10))
print(find_most_common_words('donald_speech.txt', 10))
print(find_most_common_words('melina_trump_speech.txt', 3))




        