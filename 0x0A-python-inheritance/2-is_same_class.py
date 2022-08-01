#!/usr/bin/python3
"""function that checks if object is an instance of a given class"""


def is_same_class(obj, a_class):
    """a function that checks the instance of the obj"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
