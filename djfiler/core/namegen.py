"""
#   Sina Farhadi
#
#   @2019 All Rights Served
#
#   We Genrate File Names Here :)
#
"""

from random import choice
from string import ascii_uppercase
from string import ascii_lowercase
from datetime import datetime

def generate_name():
    """
    We Generate Random Names
    """
    strst = ''.join(choice(ascii_uppercase) for i in range(20))
    strst3 = datetime.today().strftime('-%Y-%m-%d-%H-%M-%S')
    return  '{0}{1}'.format(strst, strst3)

