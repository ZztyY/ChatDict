"""
Utilities
==========
"""


def is_alphabet(uchar):
    """
    Check if uchar in alphabet
    :param uchar: an uchar
    :return: True or False if the uchar in alphabet
    """
    return '\u0041' <= uchar <= '\u005a' or '\u0061' <= uchar <= '\u007a' or uchar == '\''
