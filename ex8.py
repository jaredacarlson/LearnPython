
# Assign the string "%r %r %r %r" to a variable name formatter
# Note that this can be used as a plain string
# Or as string into which you can insert variables (%r)
# %r converts any python object to a string using repr()
formatter = "%r %r %r %r"

#prints the string formatter with the
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#StudyDrills
#2.  We used the double quotes on the string which contained an
#   apostrophe, i.e., a single quote
