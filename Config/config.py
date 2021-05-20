"""
Name: config.py
Purpose: File containing all configurable information.
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""

import uuid
import os

from datetime import date


# Logger
LOGGER_NAME = '__main__'
LOG_LEVEL = 1
LOGFILE_DIR = r'C:\Tarsium\Logs'
MAX_BYTES_PER_FILE = 500000
MAX_AMOUNT_OF_FILES = 100
ENCODE_FILE_FORMAT = 'utf8'
LOG_FORMAT = '%(asctime)s|%(name)s|%(levelname)s - %(message)s'
LOGFILE_NAME = f'TarsiumLog_{date.today()}_{uuid.uuid4()}'
LOGFILE_PATH = os.path.join(LOGFILE_DIR, LOGFILE_NAME)

# Runtime
TIMEOUT = 3
TARSIUM_INPUT_PATH = r'C:\Tarsium\Input'
INPUT_FILES_READMODE = 'rb'
SUPPORTED_INPUT_FILES_TYPES = [
    'json',
    'pcap'
]

# SQL info
DRIVER = "SQL Server"
SERVERNAME = "Nahum"
DBNAME = "Tar"
ROOT_DBNAME = "master"
JSON_TABLE_NAME = 'JSONInfo'
PCAP_TABLE_NAME = 'PCAPInfo'
TABLE_NAMES = dict(zip(SUPPORTED_INPUT_FILES_TYPES,
                       [JSON_TABLE_NAME, PCAP_TABLE_NAME]))
