# Colors
class bcolors:
    INFO = '\033[92m'
    ERROR = '\033[91m'

# Error Log
def error(info):
    print(bcolors.ERROR+'[ERROR] {}'.format(info))

# Info Log
def info(info):
    print(bcolors.INFO+'[INFO] {}'.format(info))