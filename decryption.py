# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:33:45 2024

@author: uday kumar yellaboina
"""

import re

def replace_with_original_words(encrypted_code, encrypted_words_dict):
    for encrypted_word, original_word in encrypted_words_dict.items():
        encrypted_code = encrypted_code.replace(encrypted_word, original_word)
    return encrypted_code


def decryption_after_replacing_original_words(input_string, replacement_dict):
    for key, value in replacement_dict.items():
        input_string = re.sub(r'\b' + re.escape(key) + r'\b', value, input_string)
    return input_string