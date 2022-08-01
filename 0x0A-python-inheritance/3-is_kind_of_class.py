#!/usr/bin/python3
"""check whose object a class is"""


def is_kind_of_class(obj, a_class):
    """a method to check the objects origin"""
    if isinstance(obj, a_class):
        return True
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False
