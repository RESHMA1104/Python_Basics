Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
trees = ["Mango", "Banana", "Papaya", "Pomogenerate", "Neem", "Bamboo", "Teak"]
trees
['Mango', 'Banana', 'Papaya', 'Pomogenerate', 'Neem', 'Bamboo', 'Teak']
print(type(trees))
<class 'list'>
print(len(trees))
7
print([0])
[0]
print(trees[0])
Mango
trees[6]
'Teak'
print(trees[-3])
Neem
trees.append("coconut")
trees
['Mango', 'Banana', 'Papaya', 'Pomogenerate', 'Neem', 'Bamboo', 'Teak', 'coconut']
len(trees)
8
print(trees[-3])
Bamboo
trees.insert("Lemon")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    trees.insert("Lemon")
TypeError: insert expected 2 arguments, got 1
trees.insert(6,"Lemon")
trees
['Mango', 'Banana', 'Papaya', 'Pomogenerate', 'Neem', 'Bamboo', 'Lemon', 'Teak', 'coconut']
>>> print(len(trees))
9
>>> trees.reverse()
>>> trees
['coconut', 'Teak', 'Lemon', 'Bamboo', 'Neem', 'Pomogenerate', 'Papaya', 'Banana', 'Mango']
>>> fruits = ["Apple", "Guava", "Kiwi", "Muskmelon"]
>>> trees.extend(fruits)
>>> trees
['coconut', 'Teak', 'Lemon', 'Bamboo', 'Neem', 'Pomogenerate', 'Papaya', 'Banana', 'Mango', 'Apple', 'Guava', 'Kiwi', 'Muskmelon']
>>> print(len(trees))
13
>>> type(trees)
<class 'list'>
>>> trees.remove(Papaya)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    trees.remove(Papaya)
NameError: name 'Papaya' is not defined
>>> trees.remove("Papaya")
>>> trees
['coconut', 'Teak', 'Lemon', 'Bamboo', 'Neem', 'Pomogenerate', 'Banana', 'Mango', 'Apple', 'Guava', 'Kiwi', 'Muskmelon']
>>> trees.pop(9)
'Guava'
>>> trees
['coconut', 'Teak', 'Lemon', 'Bamboo', 'Neem', 'Pomogenerate', 'Banana', 'Mango', 'Apple', 'Kiwi', 'Muskmelon']
>>> trees.index("pomogenerate")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    trees.index("pomogenerate")
ValueError: 'pomogenerate' is not in list
>>> trees.index(pomogenerate)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    trees.index(pomogenerate)
NameError: name 'pomogenerate' is not defined
>>> trees = ['coconut', 'Teak', 'Lemon', 'Bamboo', 'Neem', "Apple", 'Pomogenerate', 'Banana', 'Mango', 'Apple', 'Kiwi', 'Muskmelon', "Apple"]
>>> trees.count("Apple")
3
>>> trees.sort()
>>> trees
['Apple', 'Apple', 'Apple', 'Bamboo', 'Banana', 'Kiwi', 'Lemon', 'Mango', 'Muskmelon', 'Neem', 'Pomogenerate', 'Teak', 'coconut']
>>> trees = ['coconut', 'Teak', 'Lemon', 'Bamboo', 'Neem', 'Pomogenerate', 'Papaya', 'Banana', 'Mango', 'Apple', 'Guava', 'Kiwi', 'Muskmelon']
>>> trees.sort()
>>> 
>>> trees
['Apple', 'Bamboo', 'Banana', 'Guava', 'Kiwi', 'Lemon', 'Mango', 'Muskmelon', 'Neem', 'Papaya', 'Pomogenerate', 'Teak', 'coconut']
trees[0:12:6]
['Apple', 'Mango']
trees[1:8:4]
['Bamboo', 'Lemon']
trees[1:12:4]
['Bamboo', 'Lemon', 'Papaya']
trees.copy()
['Apple', 'Bamboo', 'Banana', 'Guava', 'Kiwi', 'Lemon', 'Mango', 'Muskmelon', 'Neem', 'Papaya', 'Pomogenerate', 'Teak', 'coconut']
forest = ("Mangolia", "South America", "Africa", "Vietnam", "Cambodia")
forest
('Mangolia', 'South America', 'Africa', 'Vietnam', 'Cambodia')
forest[0]
'Mangolia'
forest[0]="Austria"
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    forest[0]="Austria"
TypeError: 'tuple' object does not support item assignment
trees = ["Guava", "Coconut", "Bamboo"]
forest =("Mangolia", "South America", "Africa", "Vietnam", "Cambodia")
print("trees")
trees
print(treees)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(treees)
NameError: name 'treees' is not defined. Did you mean: 'trees'?
print(trees)
['Guava', 'Coconut', 'Bamboo']
print(forest)
('Mangolia', 'South America', 'Africa', 'Vietnam', 'Cambodia')
set1 = {1,2,3}
set2 = {3,4,5}
def union_set(set1, set2):
    return set1.union(set2)

def intersection_set(set1, set2):
    return set1.intersection(set2)
def symmetric_difference_set(set1, set2):
    return set1.symmetric_difference(Set2)

print("Union:", union_set(set1, set2))
Union: {1, 2, 3, 4, 5}
print("Intersection:", intersection_set(set1, set2))
Intersection: {3}

