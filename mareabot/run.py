import logging

from mareabot.api import posting

log = logging.getLogger("MareaBot")

def startup_bot():
    log.info("Start the work")
    posting()
    log.info("End the work")
