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

from .core import file_upload, logger

class DjangoFiler:
    """
    @2019

    You Can Upload Files With Non encryption or Encrypted Format With This Module
    Usage:
        djupload = Django_Upload_File_Handler(media directory here)

        then on files you can do

        djupload.upload(request.['file name upload from forms'], name=(optional), encrypy=(optional) )
    """

    # Initial Class
    def __init__(self, dest_root):
        # Uploaded Files Saves in dest_root
        self.dest = dest_root

    # Upload Function
    def upload(self, file, *args, **kwargs):
        ################ Needed Parametrs
        # Uploaded File
        file = file
        # Destination Dir
        dest = self.dest
        # Name For File (optional)
        name = None
        # Encrypt File Boolean (optional)
        encrypt = None
        # Encrypt key (optional)
        key = None
        # File Format
        frtfile = '.jpg' # Test Format

        # Get The Parametrs From Args
        for ar in args:
            try:
                file = ar.file
            except:
                logger.error('file is Needed Parameter')
            try:
                name = ar.name
                encrypt = ar.encrypt
                key = ar.key
            except:
                logger.info('Some Optional Argumant arent Passed But Not Matter')
            
        # Upload File Function        
        logger.info('Passed to Upload File Parameters')
        file_upload.upload_file(file,dest)
        