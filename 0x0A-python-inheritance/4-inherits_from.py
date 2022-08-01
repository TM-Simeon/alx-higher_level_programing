#!/usr/bin/python3
"""a function to check inheritance"""


def inherits_from(obj, a_class):
    """check if it inherited"""
    if not isinstance(obj, a_class):
        if issubclass(type(obj), a_class):
            return True
    else:
        return False
