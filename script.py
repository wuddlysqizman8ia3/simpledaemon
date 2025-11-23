#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Random Password Generator"""

import string
import random

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

if __name__ == "__main__":
    password = generate_password()
    print(f"Generated password: {password}")
    print(f"Password length: {len(password)}")
