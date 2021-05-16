import logging
from proj.TelemetryGenerator.Utils.Config import Config

from logging.handlers import RotatingFileHandler


class InitLogger:
    def __init__(self):
        self._logger = logging.getLogger(Config.LOGGER_NAME)

    @property
    def logger(self):
        self._logger.setLevel(Config.LOG_LEVEL)
        return self._logger

    def basic_logger(self):
        stream_handler = self._stream_handler_logger()
        return stream_handler

    def _stream_handler_logger(self):
        ch = logging.StreamHandler()
        ch.setLevel(Config.LOG_LEVEL)
        ch.setFormatter(self._get_formatter())
        self.logger.addHandler(ch)
        return self.logger

    def rotating_logger(self, basic_logger):
        rh = RotatingFileHandler(filename=Config.LOG_PATH_NAME,
                                 maxBytes=Config.MAX_BYTES_PER_FILE,
                                 backupCount=Config.MAX_AMOUNT_OF_FILES,
                                 encoding=Config.ENCODE_FILE_FORMAT)
        rh.setLevel(Config.LOG_LEVEL)
        rh.setFormatter(self._get_formatter())
        basic_logger.addHandler(rh)
        return basic_logger

    @staticmethod
    def _set_formatted(logging_object):
        formatter = logging.Formatter(Config.LOG_FORMAT)
        logging_object.setFormatter(formatter)
        return logging_object

    @staticmethod
    def _get_formatter():
        return logging.Formatter(Config.LOG_FORMAT)
