#logging means the each step of information of code
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) #getcwd - get current path

os.makedirs(logs_path, exist_ok=True)#create directory

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

#create of logging file by giving path name
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)