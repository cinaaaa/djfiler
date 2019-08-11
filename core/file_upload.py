"""
#   Sina Farhadi
#
#   @2019 All Rights Served
#
#   We Handle Upload Files Here
#
"""


# Import Local Modules
from . import logger, namegen

################ Parametrs
# Name For File (optional)
name = None
# Encrypt File Boolean (optional)
encrypt = None
# Encrypt key (optional)
key = None
# File Format
frtfile = 'jpg' # Test Format
# IF we not have name
generated_name = None

def upload_file(file, dest, *args, **kwargs):
    """
    We Upload Using This Function
    """
    global encrypt
    global name
    global key
    global frtfile
    global generated_name


    # Generate Name For File
    try:
        generated_name = namegen.generate_name()
        logger.info(':) Name Generated : {}'.format(generated_name))
    except:
        logger.error(':( Name Not Generated')
    


    # Get The Parametrs From Args
    for ar in args:
        try:
            file = ar.file
            dest = ar.dest
        except:
            logger.error('file and dest is Needed Parameter')
        try:
            name = ar.name
            encrypt = ar.encrypt
            key = ar.key
        except:
            logger.info('Some Optional Argumant arent Passed But Not Matter')


    # Save Files Without Encryption
    if encrypt and key:
        """
            We Uplaod Files Here encrypted with key Parameters
        """
        logger.info('uploading in encrypted type')
        
        # if we have client selected name
        if name:
            try:
                pass
            except:
                logger.error('error in uploading file with name and encrypted')
        else:
            pass



    # Save Files With Encryption
    else:
        if name:
            try:
                # Write Uploaded Chunks
                with open('{}/{}.{}'.format(dest, name, frtfile), 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                logger.info('{} Uploaded Successfully :)'.format(name))
            except:
                logger.error('OoPS {} Not Uploaded Sorry :('.format(name))

        else:
            try:
                # Write Uploaded Chunks
                with open('{}/{}.{}'.format(dest, generated_name, frtfile), 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                logger.info('{} Uploaded Successfully :)'.format(generated_name))
            except:
                logger.error('OoPS {} Not Uploaded Sorry :('.format(generated_name))
