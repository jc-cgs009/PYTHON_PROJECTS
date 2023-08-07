import logging


class Log_Gen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename="./logs/automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt="%m/%d/%y %I:%M:%S %p",
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

