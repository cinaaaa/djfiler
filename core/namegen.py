"""
#   Sina Farhadi
#
#   @2019 All Rights Served
#
#   We Genrate File Names Here
#
"""

from random import choice
from string import ascii_uppercase
from string import ascii_lowercase

def generate_name():
    """
    We Generate Random Names
    """
    strst = ''.join(choice(ascii_uppercase) for i in range(20))
    strst2 = ''.join(choice(ascii_lowercase) for i in range(10))
    return  '{0}{1}'.format(strst,strst2)

