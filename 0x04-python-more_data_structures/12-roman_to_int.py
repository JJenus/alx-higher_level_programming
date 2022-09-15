#!/usr/bin/python3

def roman_to_int(roman_string):
    rom_vals = {
            'M': 1000, 'D': 500,
            'C': 100, 'L': 50,
            'X': 10, 'V': 5, 'I': 1}
    d_val = 0
    for i in range(len(roman_string)):
        rom_val = rom_vals[roman_string[i]]
        if i != 0:
            p_val = rom_vals[roman_string[i-1]]
            if p_val < rom_val:
                rom_val -= (p_val * 2)
        d_val += rom_val
    return d_val
