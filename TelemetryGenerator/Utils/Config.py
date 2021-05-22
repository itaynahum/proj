import uuid
import logging
import os

from datetime import date


class Config:
    OUTPUT_DIRECTORY = r'C:\Tarsium\Input'
    TELEMETRY_AMOUNT_LIMITATION = 100

    TELEMETRY_NAME_FORMAT = 'Tarsium_{}_{}'
    TIMEOUT_BETWEEN_RUNS = 1

    LOGGER_NAME = 'TelemetryGenerator'
    ENCODE_FILE_FORMAT = 'utf8'
    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = '%(asctime)s|%(name)s|%(levelname)s - %(message)s'
    LOG_DIR_NAME = r'C:\TelemetryGenerator\Logs'
    LOG_FILE_NAME = f'TelemetryGenerator_{date.today()}_{uuid.uuid4()}'
    LOG_PATH_NAME = os.path.join(LOG_DIR_NAME, LOG_FILE_NAME)
    MAX_BYTES_PER_FILE = 1000000
    MAX_AMOUNT_OF_FILES = 150

    DIRECTORIES_TO_VALIDATE = [OUTPUT_DIRECTORY, LOG_DIR_NAME]
