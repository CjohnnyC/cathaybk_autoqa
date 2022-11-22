import logging
from datetime import datetime
from selfFunctions import file_path, TIME_FORMAT

NTIME=datetime.now().strftime(TIME_FORMAT)

logging.basicConfig(
    filename = file_path("./log", NTIME+".log"),
    format = '[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', 
    level = logging.INFO,
    filemode = 'a',
    datefmt = TIME_FORMAT)
