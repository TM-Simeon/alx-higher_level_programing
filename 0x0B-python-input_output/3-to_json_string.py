#!/usr/bin/python3
import json
"""a module that returns the json representation of an object"""


def to_json_string(my_obj):
    """function to convert object to json"""
    return json.dumps(my_obj)
