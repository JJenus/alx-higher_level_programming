#!/usr/bin/python3
"""5-text_indentation.py"""


def text_indentation(text):
    """text_indentation
    Args:
        text (str): printable text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if (i == 0 and text[i] == " ") or (
                text[i] == " " and (
                    text[i-1] == " " or text[i-1] == "\n")):
            continue
        print(text[i], end="")
        if text[i] in [".", "?", "?"]:
            print("\n")
