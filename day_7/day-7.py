# Exercise: Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update('Tiktok', 'Spotify', 'Netflix')
it_companies.remove('Amazon')
# it_companies.remove('Discord')
it_companies.discard('Discord')

# Exercise: Level 2

c = a.union(b)
print(c)
c = a.intersection(b)
print(c)

print(a.issubset(b))
print(a.isdisjoint(b))
print(a.union(b))
print(b.union(a))
c = a.symmetric_difference(b)
print(c)
del a
del b
# print(b)

# Exercise 3: Level 3
age_list = set(age)
print(len(age_list))
print(len(age))
