#!/usr/bin/python3
"""A function that returns the list of available attributes"""


def lookup(obj):
    """a method to return available attributes of an object"""
    return dir(obj)
