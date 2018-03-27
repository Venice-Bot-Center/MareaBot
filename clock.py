from mareabot.api import reading_api
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=7)
def timed_job():
    reading_api()


sched.start()
