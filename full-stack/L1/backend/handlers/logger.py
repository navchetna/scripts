import logging

class Logger:
    def __init__(self, module: str):
        self.log_format = "%(levelname)s | %(asctime)s |    %(module)s   | %(lineno)d | %(message)s"
        self.date_format = "%Y-%m-%d %H:%M:%S"
        self.logger = logging.getLogger(module)
        logging.basicConfig(level=logging.INFO, format=self.log_format, datefmt=self.date_format)