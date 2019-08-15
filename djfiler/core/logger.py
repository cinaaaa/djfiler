"""
#
#   Sina Farhadi
#   
#   @2019 All Rights Served
#
#   This Is Logger Code
#
#   This Module is Use To Print Debugging Process
#
"""

# Colors
class bcolors:
    INFO = '\033[94m'
    ERROR = '\033[91m'
    RESET = '\033[0m'

debug = True

def init(state):
    global debug
    debug = state

# Error Log
def error(info):
    if debug == True:
        print(bcolors.ERROR+'[ERROR] {}'.format(info))
        # Reset Terminal Color
        print(bcolors.RESET+'')

# Info Log
def info(info):
    if debug == True:
        print(bcolors.INFO+'[INFO] {}'.format(info))
        # Reset Terminal Color
        print(bcolors.RESET+'')