# coding=utf-8
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

from mareabot.api import reading_api


def set_task():
    scheduler = BackgroundScheduler()
    scheduler.add_job(reading_api, 'interval', seconds=10)
    # Shut down the scheduler when exiting the app
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())
