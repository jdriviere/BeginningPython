# ============================================
# @name BEGINNING PYTHON 3
# @author J. Djimitry Riviere
# @description Easy, simple introduction to the
#              Python 3 programming language for
#              those who want to start coding.
# @date 06-11-2018
#
# UNIT 2
# Activity 01 - Data Types
#
# NOTE:
# You don't have to change anything from the
# code below. This is an example I left for you
# to evaluate and use as a reference.
#
# SIDENOTE:
# The advantage of Python variables is that you
# don't have to declare its type, as you would
# do with other more complex programming languages.
# For instance, let's compare Java and Python:
# 
# --- JAVA ---  |  --- PYTHON ---
# int a = 30;   |  a = 30
#
# *Which one would you rather choose? ;)
#
# In any programming languages, variables should always be
# declared, first, and then attribute it a value, so that it
# can be used. Some languages even permit you to declare a
# variable without giving it a value right away. Unfortunately,
# this is NOT the case for Python!
# 
# --- JAVA ---  | --- PYTHON ---
# int a;        | a <-- This is NOT allowed! 
# a = 30;       | a = 30
# ============================================
a = 30
b = "Hello"
c = 3.5
d = True

# The method type(value) allows you to determine what kind of data type
# a variable is.
print("Value of a:", a, " - Type of value a:", type(a))
print("Value of b:", b, " - Type of value b:", type(b))
print("Value of c:", c, " - Type of value c:", type(c))
print("Value of d:", d, " - Type of value d:", type(d))

# --------------------------------------------#
# ASSIGNMENT:
# Create as many variables as you want and give
# them each a value. Then determine the type of
# each value, using the method type().
# Try to create a value like the Java example to
# see if it works. Do you receive an error, or is it
# allowed? What happens when you create a variable but
# you don't give it a value right away, then try to
# print it?
#
# OBJECTIVE:
# Although one doesn't have to tell Python what type
# of value a variable is (like other more complex
# programming languages), Python is smart enough to determine
# it and remember it for you. But what if you forget it, or
# you can't see where and how it was declared? Simply use
# the type() method!
#
# --> START YOUR ASSIGNMENT BELOW! <--
# --------------------------------------------
