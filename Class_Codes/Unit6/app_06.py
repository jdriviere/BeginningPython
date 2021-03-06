# ============================================
# @name BEGINNING PYTHON 3
# @author J. Djimitry Riviere
# @description Easy, simple introduction to the
#              Python 3 programming language for
#              those who want to start coding.
# @date 06-29-2018
#
# UNIT 6
# Activity 01 - Functions and Modules
#
# NOTE:
# You don't have to change anything from the
# code below. This is an example I left for you
# to evaluate and use as a reference.
#
# SIDENOTE:
# Creating functions are very essential to any programming
# language, because it helps you manage your code better,
# by helping you not having to repeat yourself all the time.
#
# Functions are blocks of codes that are defined and later
# invoked (or called). For instance, maybe you don't want
# to have to write codes that add two or three numbers
# together all the time. Therefore, you write a function
# for that, and then call it as many times as you want.
# The following example will show you how a function is
# defined (declared/created) and invoked -- and compared
# with our loyal friend Java:
#
# --- JAVA ---                           |   --- PYTHON ---
# public int add_num( int x, int y ) {   |   def add_num( x, y )
#   return x + y;                        |      return x + y
# }
#
# In Python, functions come in various forms:
# - Without arguments (sometimes, arguments are referred to as parameters)
# - With arguments
# - With default arguments
# - With a variable-length argument
# - Anonymous
#
# Let's explore the functions without arguments.
# 
# A function without arguments is the simplest form of function
# that exists. They are usually used when you don't want to pass
# down variables for the function to work. Let's take an
# example:
# ============================================
# ----------------------
# DEFINITION
# ----------------------
print("======================")
print("No Arguments")
print("======================")
def say_hello():
    print("Hello, World!")

# ----------------------
# INVOCATION/CALLING
# ----------------------
say_hello()

print()

# ============================================
# Here, you can see that I don't need arguments to make the function
# work, because I don't need that much control in it. But the next
# example, a function with arguments, will show you why I want to
# include an argument or two.
# ============================================
# ----------------------
# DEFINITION
# ----------------------
print("======================")
print("With Arguments")
print("======================")
def say_hello(name, idn):
    print("Name:", name, "\tID:", idn)

# ----------------------
# INVOCATION/CALLING
# ----------------------
say_hello("JD", 1234)

print()

# ============================================
# Now that I have included arguments, I have more control
# on what I want to see when my code is executed. Not only
# do I want a greeting, but I also want a name to be greeted
# and my ID number.
# But Python doesn't stop there. Python, as in many other
# programming languages, allows you to pass down default
# values to your arguments, so that if the user of the code
# doesn't bother putting arguments, when invoking the function,
# a default value would be returned. Take a look at the example
# below:
# ============================================
# ----------------------
# DEFINITION
# ----------------------
print("======================")
print("With Default Arguments")
print("======================")
def say_hello(name="Chuck Norris", idn="-----"):
    print("Name:", name, "\tID:", idn)

# ----------------------
# INVOCATION/CALLING
# ----------------------
say_hello()
say_hello("JD Riviere", 12345)

print()

# ============================================
# If you pass down (or include) arguments
# in your function definition, whenever you
# call that function, make sure your arguments
# are in the right order. Looking at the example
# above, you wouldn't want 'Chuck Norris' to be
# the ID number, or is name to be '-----', right?
# Though you wouldn't be necessarily punished for
# it, it wouldn't make sense logically, and you
# may throw off your fellow coders too. So, beware
# of the order of your arguments! ;)
#
# Lastly, we will cover the last type of function
# for this class: the Anonymous Functions, which
# are essentially functions "without a name." Sometimes,
# you may not want to create a function to compute
# something simple, and you don't want to try to find
# a name for that ever-so-simple function. That's what
# Anonymous Functions are here for. So, let's take our
# add_num() function we created earlier: you don't need
# to create a function for it, because you want a quick
# answer for a simple program.
# Let's compare Java's way to Python's way of creating
# an Anonymous Function:
#
# --- JAVA ---                                   |   --- PYTHON ---
# public interface Comparator {                  |   compare = lambda a1, a2 : a1 > a2
#   public boolean compare( int a1, int a2);     |   result = compare(2, 5)
# }                                              |   print(result)
# Comparator c = ( a1, a2 ) -> return a1 > a2;
# boolean result = c.compare(2, 5);
# System.out.println(result);
#
# Using the 'lambda' keyword allows you to create that
# Anonymous Function we've been discussion. Also, look
# at the hassle of coding you have to go through in Java
# to return a true/false for a simple function. But in
# Python, we only needed three lines!
# Let's look at a few more lambda expressions:
# ============================================
print("======================")
print("Anonymous Functions (Lambda Expression)")
print("======================")
add_num = lambda num_1, num_2 : num_1 + num_2
print("Adding 2 and 5, using a Lambda Expression:", add_num(2, 5))

say_hello_v2 = lambda : print("Hello, World! (From a Lambda Expression!)")
say_hello_v2()

print()

# ============================================
# Now that we're done talking about functions, let's jump
# straight to modules. As a refresher, let me remind you
# what a module is: it is a Python file that contains
# some code, which can be exported and then imported into
# another Python file. Most popular programming languages
# have their own way to import their modules. And most of
# them import their modules the same way, with a slightly
# different syntax. In Python, there are three ways of
# importing modules:
#
# - import <module_name>
# - from <module_name> import <module_1, ..., module_N>
# - from <module_name> import *
#
# We're going to start importing another file called
# 'import_me.py' to use it as example for all three
# import types.
# ============================================
print("======================")
print("Module Imports")
print("======================")
import import_me

age = import_me.my_age # Notice that I called the module name, and then the element I want
print("My age is:", age)


from import_me import say_hi
say_hi('Justin') # Notice I didn't have to call the module name. It's already done for me at the import

# ============================================
# NOTE:
# I won't need to use the third import funtion for several
# reasons:
#   - The import <module_name> does the job for me already
#   - It's more risky to use the wildcard (*)
#   - You only use the wildcard if you absolutely must
# ============================================


# --------------------------------------------#
# ASSIGNMENT:
# Create a function for each type of function that were discussed
# in the lession, then invoke them. Do you have any errors? If so,
# what do you think was the problem? How would you solve it?
# What's the main difference between an Anonymous Function and a
# regular function? Why choose one over the other, or when?
#
# Create another Python file (make sure the extension is '.py') and
# write a function and a variable to be exported. Import it into this
# file using one of the import statements. Then invoke that function
# and/or fetch that imported variable. Did it work? If not, why do you
# think it didn't?
#
# NOTE: Don't forget to upload your code into your Github repository
#       (if you have created an account, or already have an account)
#       once you are done! :)
#
# OBJECTIVE:
# The objective of the assignment is to ensure the student understand
# the importance of functions and modules, because the next level of
# Python programming, the Object-Oriented Programming (OOP), functions
# mainly through functions. Not understanding functions may be detrimental
# to the understanding of Classes, and other advanced concepts.
#
# --> START YOUR ASSIGNMENT BELOW! <--
# --------------------------------------------
