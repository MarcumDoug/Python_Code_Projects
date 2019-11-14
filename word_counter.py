# File: word_counter.py
# Name: Doug Marcum
# Date: 10/16/2019
# Course: DSC 510
# Assignment Number: 8.1
# Description: Program opens a text file (i.e. gettysburg.txt), calculates the total words and
#              outputs the number of occurrences of each word in the file


def main():
    """Main function opens the file, creates a dictionary, calls to the process_line function
    and the pretty_prints function."""
    count = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, count)
    print('Opening File....gettysburg.txt\nProcessing...Complete!')
    pretty_print(count)


def process_line(line, count):
    """This function imports the string library, formats the text file by stripping away punctuation, whitespaces,
    makes all of the words the same case, and splits out the words. Makes a call to the add_word function."""
    import string
    line = line.rstrip().lower().translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    add_word(words, count)


def add_word(words, count):
    """This function adds each word to the dictionary."""
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1


def pretty_print(count):
    """This function formats the printed results into a structured, easily readable format."""
    print('Length of the dictionary:', len(count), 'words')
    print(f"{'Word':20}{'Count'}")
    print(f"{'':-<26}")
    for key, value in sorted(count.items(), key=lambda item: item[1], reverse=True):
        print('{:20}{}'.format(key, value))


main()
