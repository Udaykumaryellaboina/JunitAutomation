# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:53:57 2024

@author: LENOVO
"""

from cryptography.fernet import Fernet

# Generate a secret key (keep it safe!)
secret_key = Fernet.generate_key()

# Initialize the Fernet instance with the secret key
fernet = Fernet(secret_key)

# Function to encrypt text
def encrypt_text(text):
    key = Fernet.generate_key()  # Generate a key for encryption
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(text.encode('utf-8'))  # Encrypt the text
    return key, cipher_text

# Function to decrypt text
def decrypt_text(key, cipher_text):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode('utf-8')  # Decrypt the text
    return plain_text


username  = "username "
password  = "password"
key, encrypted_username = encrypt_text(username)
key, encrypted_password = encrypt_text(password)
#encrypted_text = uploaded_text.replace(username, encrypted_username.decode('utf-8')).replace(password, encrypted_password.decode('utf-8'))