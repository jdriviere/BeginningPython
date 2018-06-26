# ============================================
# @name BEGINNING PYTHON 3
# @author J. Djimitry Riviere
# @description Easy, simple introduction to the
#              Python 3 programming language for
#              those who want to start coding.
# @date 06-24-2018
#
# UNIT 3
# Activity 01 - Data Types (Part 2)
#
# NOTE:
# You don't have to change anything from the
# code below. This is an example I left for you
# to evaluate and use as a reference.
#
# SIDENOTE:
# In Python, you can create a variable that can hold
# unlimited amount of values in a collection. And, unlike
# some other programming languages, Python "collections"
# can hold more than one type of values.
# These "collections" are called lists, tuples, and
# dictionaries. Strings, too, in a sense are part of the
# "collections," as they are a series of characters put
# together to make up that value that will be assigned
# to a variable.
# 
# --- JAVA ---             |  --- PYTHON ---
# int[] a = new int[10];   |  a = []
#
# *Which looks easier to use? ;)
#
# When comparing a more complex language, like Java, notice that
# you not only have to declare the data type of the array (list),
# but you also have to allocate the amount of space you want that
# array to have (i.e.: the number 10 in the brackets). In Python,
# you don't have to specify the amount of space you want to allocate.
# Python is very dynamic in that sense too.
#
#
# 1-1.  Declaration of a list:
#       list_name = [ val1, val2, ..., val_n-1, val_n ] <-- Leave empty if you want an empty list
#
# 1-2.  Index of a list:
#       list_name[start:end:skip]
#
# 2-1.  Declaration of a tuple:
#       tuple_name = ( val1, val2, ..., val_n-1, val_n ) <-- Leave empty if you want an empty tuple
#
# 2-2.  Index of a tuple:
#       tuple_name[start:end:skip] <-- No different than a list index
#
# 3-1.  Declaration of a dictionary:
#       dict_name = { key1: val1, key2: val2, ..., key_m: val_m, key_n: val_n } <-- Leave empty if you want an empty dictionary
#
# 3-2.  Index of a dictionary:
#       dict_name[key]
#
# ============================================
# -------------------
# LIST
# -------------------
empty_list = [] # Empty list
list_a = ['a', 'b', 'c', 'd']
list_b = ['ab', 2, 'cd', 0.3, True]

print("===========================")
print("LISTS v")
print("===========================")
print(list_a) # Prints the entire list_a
print(list_b) # Prints the entire list_b
print(list_a[3]) # Prints element at index 3, IF it exists; otherwise, you'll receive an error
print(list_b[0:3]) # Prints elements at index 0 all the way to index 3, WITHOUT including index 3
print(list_a[1:]) # Prints elements starting from index 1 all the way to the end
print(list_b[:4]) # Prints elements starting from the beginning all the way to index 4 WITHOUT including index 4
print(list_a[::2]) # Prints elements from the beginning to the end, but skips every 2

# print(list_a[4]) # This will create an error, as there is no index 4

list_a[1] = 'd'
print(list_a) # The 'b' from list_a should be changed for 'd'

list_a.append('b')
print(list_a) # The append() function adds a new element to the list

# -------------------
# TUPLE
# -------------------
empty_tuple = () # Empty tuple
tuple_a = ('a', 12, 2.03)
tuple_b = ('b', 16, 10.9, False)

print("===========================")
print("TUPLES v")
print("===========================")
print(tuple_a)
print(tuple_b)
print(tuple_a[2])
print(tuple_b[1:])

# print(tuple_a[3]) # This will create an index error, as there is no index 3
# tuple_b[2] = 27.5 # This will cause a type error, because tuples are immutable
# tuple_a.append('abc') # This will cause an attribute error, because tuples are immutable

# -------------------
# DICTIONARIES
# -------------------
dict_a = {} # Creates an empty dictionary
dict_a['one'] = 1 # Inserts, in dict_a, a key-to-value with key/index 'one' and value of 1
dict_a[2] = 'Two' # Inserts, in dict_a, a key-to-value with key/index 2 and value of 'Two'
dict_b = { 'name': 'James', 'age': 32, 'avg_hrs': 8.5, 'is_good': True }

print("===========================")
print("DICTIONARIES v")
print("===========================")
print(dict_a['one']) # Prints value for key's index of 'one'
print(dict_a[2]) # Prints value for key's index of 2
print(dict_b) # Prints keys AND values
print(dict_b.keys()) # Prints ONLY keys
print(dict_b.values()) # Prints ONLY values

# print(dict_b[1]) # <-- Will create an error, as there are NO index 1; the first index is 'name'

# -------------------
# STRINGS
# -------------------
empty_str = "" # Empty string
str_a = "I am a string!"
str_b = "Welcome to my Python class."

print("===========================")
print("STRINGS v")
print("===========================")
print(str_a)
print(str_b)
print(str_a[7]) # Prints element at index 7
print(str_b[3:]) # Prints element at indexes 3 to the end
print(str_a[:4]) # Prints elements starting from the beginning all the way to index 4 without including it
print(str_b[0:5]) # Prints elements at index 0 all the way to index 5 without including index 5
print(str_a[1:8:2]) # Prints elements from index 1 to 7, skipping 2 at a time

# --------------------------------------------#
# ASSIGNMENT:
# Create a list, a tuple, and a dictionary. Use the indexing
# that you've seen in the video, and which are given in the examples
# above, and print the results. What do you get?
# Try changing the values in the list, tuple, or dictionary, using its
# index. What happens? Do you get any errors?
# Create a string, and use the same indexing principles. What did you
# notice?
#
# OBJECTIVE:
# This lesson's objective is to make sure one understands how dynamic
# the Python language is. For the most part, you can change the value
# of a variable, unless specified (in this case, tuples values cannot
# be changed once they are declared), at any given time.
# You must also make sure you understand the differences between lists,
# tuples, and dictionaries; and how they are used.
#
# --> START YOUR ASSIGNMENT BELOW! <--
# --------------------------------------------
