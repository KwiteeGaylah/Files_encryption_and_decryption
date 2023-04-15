# Files_encryption_and_decryption
 
This program is a Python script that encrypts and decyptes files in a given directory using AES.

The Program is build by separating the functionalities into two modules (encrypt.py and decrypt.py)

1. encrypt.py: This module is reponsible to encrypt files in a directory(s) recursively. it then stores the key used to encrypt the files in a text encoded file (key.txt).

2. decrypt.py: This module uses the encyption key (key.txt) to decrypt all the files.

# Installation Instruction
First, install the required python module:

```
pip install pycryptodome
```
# Usage
The program can be executed by running the main.py module. The main file is a command line tool that interacts with the user.
```
python main.py
```
