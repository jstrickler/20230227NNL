import logging

log_format = logging.Formatter(
    '%(levelname)s %(name)s %(asctime)s %(filename)s %(lineno)d %(message)s',  # set the format for log entries
    "%x-%X",
)

logging.basicConfig(   # configure root logger
    filename="multipass.log",
)

logger = logging.getLogger()   # root logger, named root

screen_handler = logging.StreamHandler()
screen_handler.setLevel(logging.ERROR)

logger.addHandler(screen_handler)

for handler in logger.handlers:
    handler.setFormatter(log_format)

logging.error("does this work?")
logging.warning("I hope so")
logging.critical("OH NO!!!")

