import logging
import os

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class Logger:

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def warning(message):
        logging.warning(message)

    @staticmethod
    def error(message):
        logging.error(message)