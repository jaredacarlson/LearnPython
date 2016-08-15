# make a variable for a string.  The insert an integer inside a string
x = "There are %d types of people." % 10
# make a variable for the string "binary"
binary = "binary"
# make a variable for the string "don't"
do_not = "don't"
# make a variable for the sentence and then put words inside the sentences
# %s converts any python object to a string using str()
y = "Those who know %s and those who %s." % (binary, do_not) # 1.  First place a string is put inside a string


print x
print y

# print string and insert string x
print "I said: %r." % x  #2. Second place a string is put inside string
# print string and insert string y
print "I also said: '%s'." % y  #3. Third place a string is put inside a string

# set variable hilarious equal to boolean False
hilarious = False

# set variable joke_evaluation with a string that is ready to have a variable inserted
joke_evaluation = "Isn't that joke so funny?! %r"

# print variable joke_evaluation and insert variable hilarious
print joke_evaluation % hilarious  #4.  Fourth place a string is put inside a string

# set variable w equal to a string
w = "This is the left side of..."

# set variable e equal to a string
e = "a string with a right side."
#print the concatenation of variables w and e
print w + e

#Typing errors: 11

#Study Drills
#3.  There are only four places.  To be put inside a string, the object must first be converted to a string.
#4. Adding w + e concantenates or makes the two strings into one, longer string


# The conversion types are:
#
# Conversion	Meaning	Notes
# d	            Signed integer decimal.
# i	            Signed integer decimal.
# o	            Unsigned octal.	(1)
# u	            Unsigned decimal.
# x	            Unsigned hexadecimal (lowercase).	(2)
# X	            Unsigned hexadecimal (uppercase).	(2)
# e	            Floating point exponential format (lowercase).
# E	            Floating point exponential format (uppercase).
# f	            Floating point decimal format.
# F	            Floating point decimal format.
# g	            Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
# G	            Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
# c	            Single character (accepts integer or single character string).
# r	            String (converts any python object using repr()).	(3)
# s	            String (converts any python object using str()).	(4)
# %	            No argument is converted, results in a "%" character in the result.	
