import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(levelname)s    \t# %(asctime)s # %(message)s")

file_handler = logging.FileHandler("debug.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
