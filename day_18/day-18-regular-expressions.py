# Day 18 - Regular Expressions
# Exercises: Level 1
# 1

import re
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = re.findall(r"\b\w+\b", paragraph, re.I)
counter = Counter(words)
words_count = sorted(counter.items(), key=lambda x: x[1], reverse=True)
print(words_count)

# 2
text = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 
0 at origin, 4 and 8 in the positive direction."""

numbers = re.findall(r"-?\d+", text)  
numbers = list(map(int, numbers))  # convert to integers
print("Extracted numbers:", numbers)

min_num = min(numbers)
max_num = max(numbers)

distance = max_num - min_num
print("Distance between furthest particles:", distance)


# Exercises: Level 2
import keyword

def is_valid_variable(var):
    pattern = r'^[A-Za-z_]\w*$'

    print (True if re.match(pattern, var) and var not in keyword.kwlist else False)

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True


# Exercise: Level 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sentence):
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", sentence)
    return cleaned


def most_frequent_words(paragraph):
    words = re.findall(r"\b\w+\b", paragraph, re.I)
    counter = Counter(words)
    words_count = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return [(count, word) for word, count in words_count[:3]]


print(clean_text(sentence)) # I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print(most_frequent_words(clean_text(sentence))) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
