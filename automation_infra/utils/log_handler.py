import datetime
import sys

from loguru import logger

from common.common import ROOT_PATH


class LoggingSettings:
    def __init__(self, log_level, log_path):
        self.log_level = log_level
        self.log_path = log_path

    def configure_logs(self):
        logger.remove()
        file_name = datetime.datetime.now().strftime("%Y_%m%d_%H_%M_%S")
        log_file_path = f"{ROOT_PATH}/{self.log_path}/{file_name}.log"
        logger.add(log_file_path, level=self.log_level)
        logger.add(sys.stdout, level=self.log_level)