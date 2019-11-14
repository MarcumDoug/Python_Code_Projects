# File: word_counter_write_file.py
# Name: Doug Marcum
# Date: 10/22/2019
# Course: DSC 510
# Assignment Number: 9.1
# Description: Program opens and reads a text file (i.e. gettysburg.txt), calculates the total words,
#              outputs the number of occurrences of each word in the text to a new file.

import string


def main():
    """Main function opens/reads the file, creates a dictionary, calls to the process_line function,
    makes certain the new file is a text file, and calls the process_file function."""
    count = {}
    with open('gettysburg.txt', 'r') as gba_file:
        for line in gba_file:
            process_line(line, count)
    print(f'Opening File....{gba_file.name}\n'
          'Processing....Complete!')
    new_file = str(input('Please enter the new text file name: ')).rstrip()
    if new_file.endswith('.txt'):
        new_file = new_file
    else:
        new_file = new_file + '.txt'
    process_file(count, new_file)
    print(f"Your file '{new_file}' has been created.")


def process_line(line, count):
    """This function formats the text file by stripping away punctuation, whitespaces, makes all of
    the words the same case, and splits out the words. Makes a call to the add_word function."""
    line = line.rstrip().lower().translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    add_word(words, count)


def add_word(words, count):
    """This function adds each word to the dictionary and counts the occurrences."""
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1


def process_file(count, new_file):
    """This function writes the results to a new text file in a structured, readable format."""
    with open(new_file, 'w') as wf:
        wf.write('Original Text: gettysburg.txt\n'
                 f'Length of the dictionary: {len(count)} words\n'
                 f"{'Word':20}{'Count'}\n"
                 f"{'':-<26}\n")
        for key, value in sorted(count.items(), key=lambda item: item[1], reverse=True):
            wf.write(f"{key:20}{value}\n")


main()
