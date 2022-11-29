import logging
import os
import webbrowser



webbrowser.open_new("https://www.unl.edu.ec/")
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, 'OpenLink.log')

#Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)


def do_loggin():
    webbrowser.open_new("https://www.unl.edu.ec/")
    logger.info('OpenLink.py executed')

if __name__ == '__main__':
    do_loggin()
