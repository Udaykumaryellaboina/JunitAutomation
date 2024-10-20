# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:44:30 2024

@author: LENOVO
"""

import hashlib

def encrypt_string_usinghashlib(input_string):
    # Use SHA-256 hashing to generate a fixed-length hash
    hash_object = hashlib.sha256(input_string.encode())
    hex_dig = hash_object.hexdigest()
    # Take the first 'n' characters of the hash, where 'n' is the length of the input string
    encrypted_string = hex_dig[:len(input_string)]
    return encrypted_string