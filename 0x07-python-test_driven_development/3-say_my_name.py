#!/usr/bin/python3
"""Third task in test driven programming """


def say_my_name(first_name, last_name=""):
    """say_my_name function
    Args:
        first_name (str): First name
        last_name (str): Last name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
