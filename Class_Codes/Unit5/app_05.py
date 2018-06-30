# ============================================
# @name BEGINNING PYTHON 3
# @author J. Djimitry Riviere
# @description Easy, simple introduction to the
#              Python 3 programming language for
#              those who want to start coding.
# @date 06-29-2018
#
# UNIT 5
# Activity 01 - Conditional Statements and Loops
#
# NOTE:
# You don't have to change anything from the
# code below. This is an example I left for you
# to evaluate and use as a reference.
#
# SIDENOTE:
# There are times, when programming, in which you
# want certain code to run when specific conditions
# are met. That's why you would find, in most programming
# languages, conditional statements (or the decision making
# process). The most widely known are the IF statement,
# IF-ELSE (or jyst ELSE) statement, and the ELSE-IF (which
# comes in various forms, depending on the language
# you use - in our case, which is Python, it would be ELIF).
#
# When you use the IF statement, the interpreter (the
# behind-the-scene executor of your code) will only execute
# the code only if a condition is met. If not, it will not
# run that code at all. Let's look at the example below:
#
# --- JAVA ---                                |   --- PYTHON ---
# int age = 28;                               |   age = 28
# if (age >= 18) {                            |   if age >= 18:
#   system.out.println("You're an adult");    |       print("You're an adult")
# }
#
# The print() function will not execute at all unless
# the variable 'age' is greater than or equal to 18.
#
# On the other hand, most programming languages allow you
# to have different alternatives, in that it allows you
# to make more than one decision. This is why you have
# an ELSE statement (see the example below). The ELSE (or
# IF-ELSE) statement essentially says, in plain English:
# "IF the condition is right, run this code; OTHERWISE/ ELSE,
# run this other code instead."
#
# --- JAVA ---                                  |   --- PYTHON ---
# int age = 28;                                 |   age = 28
# if ( age >= 18 ) {                            |   if age >= 18:
#   system.out.println( "You're an adult" );    |       print( "You're an adult" )
# } else {                                      |   else:
#   system.out.println( "You're too young" );   |       print( "You're too young" )
# }
#
# Lastly, sometimes you just want more than two alternatives (IF or ELSE),
# and use the ELSE statement as the very last resort. This is what the
# ELSE-IF/ELIF statement is for. This type of condition allows you to have
# more than two alternatives. The example below shows you how to use the
# ELIF statement in Python. Compare it to how it's used, and differs, in
# the Java programming language.
#
# --- JAVA ---                                      |   --- PYTHON ---
# int age = 28;                                     |   age = 28
# if ( age >= 18 ) {                                |   if age >= 18:
#   system.out.println( "You're an adult" );        |       print( "You're an adult" )
# } else if ( age >= 15 ) {                         |   elif age >= 15:
#   system.out.println( "You're getting there" );   |       print( "You're too young" )
# } else {                                          |   else:
#   system.out.println( "You're a child" )          |       print( "You're a child" )
# }
#
# Don't you think Python is so much simpler, with less to write and
# more to remember? ;)
#
# ============================================
print("--------------------------------")
print("IF Statement")
print("--------------------------------")
var_1 = 36
var_2 = 28

print("Variable 1:", var_1, " - Variable 2:", var_2)
if var_1 > var_2:
    print("Inside IF statement was executed because Variable 1 was greater than Variable 2!")

print()

print("--------------------------------")
print("IF-ELSE Statement")
print("--------------------------------")
var_1 = 55
var_2 = 76

print("Variable 1:", var_1, " - Variable 2:", var_2)
if var_1 > var_2:
    print("IF statement was executed because Variable 1 was greater than Variable 2!")
else:
    print("ELSE statement was executed because Variable 1 was less than Variable 2!")

print()

print("--------------------------------")
print("ELIF Statement")
print("--------------------------------")
var_1 = 88
var_2 = 88

print("Variable 1:", var_1, " - Variable 2:", var_2)
if var_1 > var_2:
    print("IF statement was executed because Variable 1 was greater than Variable 2!")
elif var_1 == var_2:
    print("ELIF statement was executed because Variable 1 and 2 are equal!")
else:
    print("ELSE statement was executed because Variable 1 was less than Variable 2!")


# Loops are very important in Python, as they allow you to run a code
# more than once at a time, or to run it indefinitely until a condition
# is met. Python offers 3 (three) main types of loops: the WHILE loop,
# the WHILE-ELSE loop, and the FOR loop.
#
# WHILE loops is the type of loop that allows you to run a code
# indefinitely, until a condition is met. While it is very useful,
# in the instance you want an infinite loop (e.g.: servers), if
# it is not properly managed, it may crash your computer program,
# or even your computer. The example below shows you how to use a
# WHILE loop.
#
# --- JAVA ---                      |   --- PYTHON ---
# int count = 0;                    |   count = 0
# while ( count <= 5 ) {            |   while count <= 5:
#   system.out.println( count );    |       print( count )
#   count++;                        |       count += 1
# }
#
# A WHILE loop usually ensures that the code in its body executes at least once.
#
# The next type of loop is the WHILE-ELSE loop. It is a conditional
# statement and a flow control mixed together. Prior to the execution
# of the loop, it will evaluate the condition and run the appropriate
# alternative path. The example below shows you how it's done.
#
# --- PYTHON ---
# count = 0
# while count <= 5:
#   print(count)
#   count += 1
# else:
#   print("Count is too high!")
#
# Did you notice that, this time, I didn't put any Java code? That's
# because Java doesn't have a WHILE-ELSE loop. Although it does have
# another WHILE loop, which is the DO-WHILE--but it is a completely
# different thing, and you don't need to worry about that. ;)
#
#
# The next type of loop is the FOR loop, which allows you to iterate
# through a sequence -- more so lists, tuples, ranges, or even strings.
# Unlike WHILE loops, FOR loops are limited by the range of the values
# it has to iterate through -- meaning that you can't use FOR loops
# to create infinite loops. Let's evaluate the example below and
# compare it to Java:
#
# --- JAVA ---                                  |   --- PYTHON ---
# int[] list_a = [1, 2, 3, 4, 5];               |   list_a = [1, 2, 3, 4, 5]
# for ( int i = 0; i < list.length(); i++ ) {   |   for i in list_a:
#   system.out.println( list_a[i] );            |       print( i )
# }
#
# So much simple to use Python, when it comes to FOR loops. ;)
#
# Let's try to compare how to go through and print each character found in
# a string.
#
# --- JAVA ---                                   |   --- PYTHON ---
# String str_a = "Hello, World!";                |   str_a = "Hello, World!"
# for ( int i = 0; i < str_a.length(); i++ ) {   |   for char in str_a:
#   char letter = str_a.charAt( i );             |       print( char )
#   system.out.println( letter );
# }
#
# Python goes straight to business. No need for extra variables or
# functions just to compute a simple task. ;)
#
# ============================================
pass

# --------------------------------------------#
# ASSIGNMENT:
# Your assignment is to come up with a program (just a few lines of
# code) that will run/execute if a condition of your choice is met.
# You're free to choose whatever condition you want to implement,
# but make sure you use all the conditional statements we've gone
# over in the videos and the examples above (i.e.: IF, IF-ELSE, and
# ELIF statements).
# Once you're done, how about doing the same thing, but with the loops
# we've talked about in the videos (meaning, WHILE loops, WHILE-ELSE
# loops, and FOR loops). Make sure you use the examples as guide; and
# above all, watch out for infinite loops, as they can cause your
# computer to crash, if they are not properly managed.
#
# If you happen to have accidentally create one, press CTRL + C,
# CTRL + D, or CTRL + Z in order to force-terminate your code.
#
# NOTE: Don't forget to upload your code into your Github repository
#       (if you have created an account, or already have an account)
#       once you are done! :)
#
# OBJECTIVE:
# The objective of the assignment is to introduce you to the flow control
# concepts, as they allow a programmer to control the way a code executes
# and when it would execute. It is also important to understand when one
# should you a WHILE loop over a FOR loop. In some cases, one is more
# advantageous to use than the other. Understanding control flow is a
# step-up to most concepts that have been discussed in previous lessons.
#
# --> START YOUR ASSIGNMENT BELOW! <--
# --------------------------------------------
