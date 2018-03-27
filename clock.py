from apscheduler.schedulers.blocking import BlockingScheduler

from mareabot.api import reading_api

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=7)
def timed_job():
    reading_api()


sched.start()
