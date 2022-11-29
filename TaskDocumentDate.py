import logging
import os
import webbrowser



dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, 'GenerateTimeDate.log')

#Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)


def do_loggin():
    logger.info('Generate Date')

if __name__ == '__main__':
    do_loggin()

