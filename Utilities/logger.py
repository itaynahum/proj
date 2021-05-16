"""
Name: logger.py
Purpose: Rotating logger creator
Owner: Itay Nahum
Log Date: 22:50:00 15/05/21
"""
import logging
import proj.Config.config as cfg

from logging.handlers import RotatingFileHandler


class InitRotatingLogger:
    def __init__(self):
        self._logger = logging.getLogger(cfg.LOGGER_NAME)

    @property
    def logger(self):
        self._logger.setLevel(cfg.LOG_LEVEL)
        return self._logger

    def get_logger(self):
        """
        Main function - handles the creation of rotating logger.
        :return: Rotating logger
        """
        rotating_handler = self._create_rotating_logger()
        return rotating_handler

    @staticmethod
    def _build_logger(level, formatter, base_logger, new_object):
        new_object.setLevel(level)
        new_object.setFormatter(formatter)
        base_logger.addHandler(new_object)
        return base_logger

    def _create_rotating_logger(self):
        ch = logging.StreamHandler()
        self._build_logger(cfg.LOG_LEVEL, self._get_formatter(), self.logger, ch)
        rotating_logger = self._rotating_logger(self.logger)
        return rotating_logger

    def _rotating_logger(self, basic_logger):
        rh = RotatingFileHandler(filename=cfg.LOGFILE_PATH,
                                 maxBytes=cfg.MAX_BYTES_PER_FILE,
                                 backupCount=cfg.MAX_AMOUNT_OF_FILES,
                                 encoding=cfg.ENCODE_FILE_FORMAT)
        built_rotating_logger = self._build_logger(cfg.LOG_LEVEL, self._get_formatter(),
                                                   basic_logger, rh)
        return built_rotating_logger

    @staticmethod
    def _set_formatted(logging_object):
        formatter = logging.Formatter(cfg.LOG_FORMAT)
        logging_object.setFormatter(formatter)
        return logging_object

    @staticmethod
    def _get_formatter():
        return logging.Formatter(cfg.LOG_FORMAT)
