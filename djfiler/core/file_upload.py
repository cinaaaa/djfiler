"""
#   Sina Farhadi
#
#   @2019 All Rights Served
#
#   We Handle Upload Files Here :)
#
"""


# Import Local Modules
from . import logger, namegen
import json

################ Parametrs
dest = 0
name = 0
# File Format
frtfile = 0
# IF we not have name
generated_name = 0

def upload_file(file, dest,**kwargs):
    """
    We Upload Using This Function
    """
    global frtfile
    global generated_name
    global name


    for keys, value in kwargs.items():
        if str(keys) == 'name': name = value

    logger.info('all parameters Passed {}'.format(name))


    # Get The File Format
    frtfile = file.name.rsplit('.', 1)[1]
    

    if name != 0 and name != '':
        try:
            # Write Uploaded Chunks
            with open('{}/{}.{}'.format(dest, name, frtfile), 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            logger.info('{} Uploaded Successfully :) to {}'.format(name, dest))
            try:
                callback = {'status':'ok', 'name': '{}'.format(name), 'type':frtfile }
                return json.dumps(callback)
            except:
                logger.error('We Couldent Return Status Of Your Process :(')
        except:
            logger.error('Oops {} Not Uploaded Sorry :('.format(name))
            try:
                callback = {'status':'fail'}
                return json.dumps(callback)
            except:
                logger.error('We Couldent Return Status Of Your Process :(')

    else:
        # Generate Name For File
        try:
            generated_name = namegen.generate_name()
            logger.info(':) Name Generated : {}'.format(generated_name))
        except:
            logger.error(':( Name Not Generated')
        
        try:
            # Write Uploaded Chunks
            with open('{}/{}.{}'.format(dest, generated_name, frtfile), 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            
            logger.info('{} Uploaded Successfully :) to {}'.format(generated_name, dest))
            # Return Status
            try:
                callback = {'status':'ok', 'name': '{}'.format(generated_name), 'type':frtfile }
                return json.dumps(callback)
            except:
                logger.error('We Couldent Return Status Of Your Process :(')
        except:
            logger.error('Oops {} Not Uploaded Sorry :('.format(generated_name))
            try:
                callback = {'status':'fail'}
                return json.dumps(callback)
            except:
                logger.error('We Couldent Return Status Of Your Process :(')
