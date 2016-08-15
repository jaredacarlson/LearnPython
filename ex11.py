#Exercise 11: Asking Questions

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Note:
# We put a , (comma) at the end of each print line. This is so print doesn't
# end the line with a newline character and go to the next line.

# STUDY DRILLS
#  1. Python's Raw Input
#   raw_input([prompt])
#   If the prompt argument is present, it is written to standard output without a trailing newline.
#   The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:
#
#   >>>
#   >>> s = raw_input('--> ')
#   --> Monty Python's Flying Circus
#   >>> s
#   "Monty Python's Flying Circus"
#   If the readline module was loaded, then raw_input() will use it to provide elaborate line editing and history features.

# 2. Can you find other ways to use it?  Try some of the examples you find.
age2 = raw_input('How old are you again? ')
print "Oh, you are %r years old." % age2

#3. Write another "form" like this to ask some other Questions
print "What is your most enjoyable hobby?",
hobby = raw_input()
print "Do you watch any television shows regularly?",
shows1 = raw_input()
if shows1 == 'yes':
    print "Which shows do you watch?",
    shows2 = raw_input()
else:
    print "What do you like to do instead of watching television in the evening?",
    shows2 = raw_input()
print "Ok.  Your most enjoyable hobby is %r and you like to watch %r." % (
    hobby, shows2)

#4. Escape Sequences
# Related to escape sequences, try to find out why the last line has '6\'2"' with
# that \' sequence. See how the single-quote needs to be escaped because otherwise it would end the string?

# It must not be using %s to print ?????
