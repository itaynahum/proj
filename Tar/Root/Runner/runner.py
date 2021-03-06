"""
Name:runner.py
Purpose: The main runner of the program - raises Critical exception if needed.
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""

import sys
import time
import requests

from Utilities.consts import *
from Config.config import FULL_PATH

class Runner:
    """
    Runner class. handles the running method and sleeping method of the program.
    """
    def __init__(self, timeout, handler, logger):
        self.timeout = timeout
        self.handler = handler
        self.logger = logger 

    def sleep(self):
        self.logger.info(SLEEP_LOG.format(self.timeout))
        time.sleep(self.timeout)

    def run(self):
        while True:
            try: 
                self.logger.info(RUNNING_LOG)
                self.handler.handle()
            except Exception as error:
                self.logger.critical(msg=sys.exc_info())
                self.logger.critical(error)
                raise
            self.sleep()


