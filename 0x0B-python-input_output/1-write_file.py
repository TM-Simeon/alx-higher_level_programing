#!/usr/bin/python
""" A function that writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    count = 0
    with open(filename, "w", encoding="utf-8") as f:
        for line in text:
            count += 1
        f.write(text)
    return count
