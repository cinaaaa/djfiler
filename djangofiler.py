"""
#   Sina Farhadi
#
#   @2019 All Rights Served
#
#   Django Filer v 0.1
#
#   github = https://github.com/E-RROR/django-file-uplaod-handler
#
#   All Files Supports :)
#
"""
import json
from .core import file_upload, logger, founder


# Some Of Needed Parameters
name = 0


class Filer:
    """
    @2019
    You Can Upload Files With Non encryption or Encrypted Format With This Module
    See https://github.com/E-RROR/django-filer for Examples and more info
    """

    # Initial Class
    def __init__(self, dest_root: 'destination path', debug: 'Mode Of Debug Process'):
        self.dest = dest_root
        # Set The Logger Mode
        if debug != True : logger.init(0)
        if debug == True : logger.info('You See Log Messages Because Debug Mode is True')
        logger.info('''
            Uploader Initialized Successfully :) with this params
            \n
            destination = {} \n
            debug mode = {} \n
            '''.format(dest_root, debug))

    # Upload Function
    def upload(self, file, **kwargs):
        """
        We Upload Files in This Function with file_uplaod
        """
        ################ Needed Parameters
        global name
        # Destination Dir
        dest = self.dest
        # Encrypt File Boolean (optional)
        # Get The Parametrs From Args
        for keys, value in kwargs.items():
            if str(keys) == 'name': name = value

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

