from sys import argv  # argv is the argument variable from the sys module

# script, first, second, third = argv   #unpacks argv.  Argv gets assigned to
                                        #four variables.
#
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third


#Study Drills

# script, first, second = argv
# print "You ran the script:", script
# print "You like to:", first
# print "You hate to:", second


# script, first, second, third, fourth = argv
#
# print "This is the script:", script
# print "You want to go to:", first
# print "You went to:", second
# print "You live in:", third
# print "You want to live in:", fourth

#3. Script with raw_input and argv

script, question = argv

answer = int(raw_input(question))

if answer > 40:
    print "You're huge!"
else:
    print "You should put on a little weight!"



#4. Modules give you features!
