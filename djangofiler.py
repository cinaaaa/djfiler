"""
#   Sina Farhadi
#
#   @2019 All Rights Served
#
#   Django File Upload Handler v 0.1
#
#   https://github.com/E-RROR/django-file-uplaod-handler
#
#   All Files Supports
#
"""
import json
from .core import file_upload, logger, founder


# Some Of Needed Parameters
name = 0
encrypt = 0
key = 0


class DjangoFiler:
    """
    @2019
    You Can Upload Files With Non encryption or Encrypted Format With This Module
    Usage:
    """

    # Initial Class
    def __init__(self, dest_root: 'destination path', sec_key: 'Django secret key to encrypt files', debug: 'Mode Of Debug Process'):
        self.dest = dest_root
        self.key = sec_key
        # Set The Logger Mode
        if debug != True : logger.init(0)
        if debug == True : logger.info('You See Log Messages Because Debug Mode is True')
        logger.info('''
            Uploader Initialized Successfully :) with this params
            \r\n
            destination = {} \r\n
            secretkey = {}   \r\n
            debug mode = {} \r\n
            '''.format(dest_root, sec_key, debug))

    # Upload Function
    def upload(self, file, **kwargs):
        """
        We Upload Files in This Function with file_uplaod
        """
        ################ Needed Parameters
        global name
        global key
        global encrypt
        # Destination Dir
        dest = self.dest
        # Encrypt File Boolean (optional)
        # Get The Parametrs From Args
        for keys, value in kwargs.items():
            if str(keys) == 'name': name = value
            if str(keys) == 'encrypt': encrypt = value
            if str(keys) == 'key': key = value

        # Upload File Function        
        logger.info('Passing to Upload File Parameters')
        fileupload = file_upload.upload_file(file,dest, name=name)
        return fileupload

    # FIND Files Here
    def find(self, key: 'key of the requested file'):
        """
        @2019
        Files Find And Returned Here
        """
        logger.info('Passing Parameters to Found And Return')
        # Founder Function
        fidn = founder.findfile(self.dest, key)
        # Return Founder Stuff Final
        return fidn

