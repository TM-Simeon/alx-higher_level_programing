#!/usr/bin/python3
"""a function to check inheritance"""


def inherits_from(obj, a_class):
    """check if it inherited"""
    return type(obj) != a_class and issubclass(type(obj), a_class)
