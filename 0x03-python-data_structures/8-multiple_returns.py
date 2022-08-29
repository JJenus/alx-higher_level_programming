#!/usr/bin/python3

def multiple_returns(sentence):
    s_len = len(sentence)
    cha = sentence[0] if s_len > 0 else None

    return (s_len, cha)
