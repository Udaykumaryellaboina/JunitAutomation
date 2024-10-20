# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:55:40 2024

@author: uday kumar yellaboina
"""
import javalang
import pyaes
import os

# Generate a secret key (keep it safe!)
def encrypt_java_code_elements(java_code):
    global encrypted_words_dict  # Access global decryption_map
    key = os.urandom(32)
    encrypted_code = java_code
    tree = javalang.parse.parse(java_code)
    
    # Encrypt class names
    for path, node in tree:
        if isinstance(node, javalang.tree.ClassDeclaration):
            original_class_name = node.name
            encrypted_class_name = encrypt_string(original_class_name, key)
            encrypted_words_dict[encrypted_class_name] = original_class_name
            encrypted_code = encrypted_code.replace(original_class_name, encrypted_class_name)
    
    # Encrypt method names
    for path, node in tree:
        if isinstance(node, javalang.tree.MethodDeclaration):
            original_method_name = node.name
            encrypted_method_name= encrypt_string(original_method_name, key)
            encrypted_words_dict[encrypted_method_name] = original_method_name
            encrypted_code = encrypted_code.replace(original_method_name, encrypted_method_name)
            
    
    # Encrypt variable names
    for path, node in tree:
        if isinstance(node, javalang.tree.VariableDeclarator):
            original_variable_name = node.name
            encrypted_variable_name = encrypt_string(original_variable_name, key)
            encrypted_words_dict[encrypted_variable_name] = original_variable_name
            encrypted_code = encrypted_code.replace(original_variable_name, encrypted_variable_name)
    
    # Encrypt string literals
    for path, node in tree:
        if isinstance(node, javalang.tree.Literal) and isinstance(node.value, str):
            original_string = node.value
            encrypted_string = encrypt_string(original_string, key)
            encrypted_words_dict[encrypted_string] = original_string
            encrypted_code = encrypted_code.replace(original_string, encrypted_string)
            
    # Encrypt method invocation names
    for path, node in tree:
        if isinstance(node, javalang.tree.MethodInvocation):
            original_invocation_name = node.member
            encrypted_invocation_name = encrypt_string(original_invocation_name, key)
            encrypted_words_dict[encrypted_invocation_name] = original_invocation_name
            encrypted_code = encrypted_code.replace(original_invocation_name, encrypted_invocation_name)
            
            for parameter in node.arguments:
                if isinstance(parameter, javalang.tree.VariableDeclarator):
                    original_parameter_name = parameter.name
                    encrypted_parameter_name = encrypt_string(original_parameter_name, key)
                    encrypted_words_dict[encrypted_parameter_name] = original_parameter_name
                    encrypted_code = encrypted_code.replace(original_parameter_name, encrypted_parameter_name)
                    
    # Encrypt field declarations
    for path, node in tree:
        if isinstance(node, javalang.tree.FieldDeclaration):
            original_field_name = node.declarators[0].name
            encrypted_field_name= encrypt_string(original_field_name, key)
            encrypted_words_dict[encrypted_field_name] = original_field_name
            encrypted_code = encrypted_code.replace(original_field_name, encrypted_field_name)
            
    # Encrypt constructor declarations
    for path, node in tree:
        if isinstance(node, javalang.tree.ConstructorDeclaration):
            original_constructor_name = node.name
            encrypted_constructor_name= encrypt_string(original_constructor_name, key)
            encrypted_words_dict[encrypted_constructor_name] = original_constructor_name
            encrypted_code = encrypted_code.replace(original_constructor_name, encrypted_constructor_name)
            
    # Encrypt interface declarations
    for path, node in tree:
        if isinstance(node, javalang.tree.InterfaceDeclaration):
            original_interface_name = node.name
            encrypted_interface_name = encrypt_string(original_interface_name, key)
            encrypted_words_dict[encrypted_interface_name] = original_interface_name
            encrypted_code = encrypted_code.replace(original_interface_name, encrypted_interface_name)
            
    # Encrypt annotation declarations
    for path, node in tree:
        if isinstance(node, javalang.tree.AnnotationDeclaration):
            original_annotation_name = node.name
            encrypted_annotation_name= encrypt_string(original_annotation_name, key)
            encrypted_words_dict[encrypted_annotation_name] = original_annotation_name
            encrypted_code = encrypted_code.replace(original_annotation_name, encrypted_annotation_name)
            
    # Encrypt enum declarations
    for path, node in tree:
        if isinstance(node, javalang.tree.EnumDeclaration):
            original_enum_name = node.name
            encrypted_enum_name = encrypt_string(original_enum_name, key)
            encrypted_words_dict[encrypted_enum_name] = original_enum_name
            encrypted_code = encrypted_code.replace(original_enum_name, encrypted_enum_name)
            
    # Encrypt parameter names
    for path, node in tree:
        if isinstance(node, javalang.tree.FormalParameter):
            original_parameter_name = node.name
            encrypted_parameter_name= encrypt_string(original_parameter_name, key)
            encrypted_words_dict[encrypted_parameter_name] = original_parameter_name
            encrypted_code = encrypted_code.replace(original_parameter_name, encrypted_parameter_name)
           
        # Encrypt variable names in assignments
    return encrypted_code

def encrypt_string(input_string, key):
    if key is None:
        key = os.urandom(32)  # 256-bit key

    aes = pyaes.AESModeOfOperationCTR(key)
    input_bytes = input_string.encode('utf-8')
    encrypted_bytes = aes.encrypt(input_bytes)
    encrypted_bytes = encrypted_bytes.hex()
    encrypted_string = encrypted_bytes[:len(input_string)]
    return encrypted_string