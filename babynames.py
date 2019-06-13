#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    names = []
    girl_names = []
    boy_names = []
    with open(filename, 'r') as data:
        text = data.read()
        year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text) # search only allows for one parameter
        name_match = re.finditer(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    for name in name_match:
        girl_names.append(name.group(3,1))
        boy_names.append(name.group(2,1))
    if not year_match:
        print("Couldn't find the year")
    year = year_match.group(1)
    names.append(year)
    full_list = boy_names + girl_names
    sorted_list = sorted(full_list, key = lambda x: x[0])

    str_list = []
    for tuple_temp in sorted_list:
        str_list.append(str(tuple_temp[0] + ' ' + str(tuple_temp[1])))
    formatted_list = '\n'.join(str_list) + '\n'

    print formatted_list
    
    # print str_list. this is a longer version of above code.
    # print formatted_list
    # sorted_girls = sorted(girl_names, key= lambda x:[1])
    # sorted_boys = sorted(boy_names, key= lambda x:[1])


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = args.files

    # option flag
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    
    create_summary = args.summaryfile
    if create_summary:
        for i in file_list:
            with open(i+'.summary', 'w+') as a_file:
                a_file.write(extract_names(i))
        else:
            for i in file_list:
                print extract_names(i)


extract_names('baby1990.html')

if __name__ == '__main__':
    main()
