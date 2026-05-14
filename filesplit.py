### m03g/filesplit.py
import sys

# Grab the book filename from the command line
if (len(sys.argv) == 2):
    book = sys.argv[1]
else:
    sys.exit("Usage: python3 script32.py book.txt")

# Read the entire book as a string (and close the open file)
with open('txts/' + book) as my_open_book:
    the_book = my_open_book.read()

# Create and process a worklist of the form: narrative, dialog, narrative, ...

print("\nThe End.")