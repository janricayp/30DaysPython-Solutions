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
