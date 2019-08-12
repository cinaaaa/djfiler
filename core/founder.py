"""
#   Sina Farhadi
#
#   @2019 All Rights Served
#
#   We Found and Returns Url Of Files Here
#
"""
from . import namegen, logger
import os, glob
import json


def findfile(dest, key):
    """
    Main Func to Find and Return Avability
    """
    entries = os.listdir(dest)
    logger.info('listing {} directory'.format(dest))
    try:
        # Found File
        for entry in entries:
            # Check File Name For That We Want
            before = entry.split('.')[0]
            after = entry.split('.')[1]
            if before == key:
                logger.info('{}.{} is found'.format(key, after))
                callback = {'find': 'find', 'uri':'{}/{}.{}'.format(dest,before,after) ,'type': after }
                return json.dumps(callback)
    except:
        logger.error('We Cant List {}'.format(dest))
        callback = {'find': 'no'}
        return json.dumps(callback)

    
