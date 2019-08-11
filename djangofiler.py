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

name = 0
encrypt = 0
key = 0


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
    def upload(self, file, **kwargs):
        ################ Needed Parametrs
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
        file_upload.upload_file(file,dest, name=name, encrypt=encrypt, key=key)
        