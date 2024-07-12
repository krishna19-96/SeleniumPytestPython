import logging


def log_checks():
    logging.basicConfig(
        filename="logs.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S - %p'
    )
    return logging.getLogger()
#
# logger = log_checks()
# logger.info("Start")
# logger.info("Hi")
# logger.info("Stop")
