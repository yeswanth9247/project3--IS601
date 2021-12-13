""" Builds Log File  """
import logging

# pylint: disable=line-too-long,unspecified-encoding,logging-fstring-interpolation,f-string-without-interpolation

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
fhandler = logging.FileHandler('test.log')
fhandler.setFormatter(f)
log.addHandler(fhandler)
logging.info("Processing...")


def output_data(filename, valuea, sign, valueb, valuec):
    """ Building template for the log file """
    log.debug(f'Looping through {filename} now...')
    with open('test.log', 'a') as append_outfile:
        append_outfile.write(f'Filename:{filename} - ValueA:{valuea} {sign} ValueB:{valueb} = {valuec}\n')
    return append_outfile


log.info(f"Thanks for verifying your CSV with me!")
