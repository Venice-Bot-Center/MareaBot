from loguru import logger

from mareabot.api import posting


def startup_bot():
    logger.info("Start the work")
    posting()
    logger.info("End the work")
