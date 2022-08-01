#!/usr/bin/python3
"""a function to check inheritance"""


def inherits_from(obj, a_class):
    """check if it inherited"""
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
