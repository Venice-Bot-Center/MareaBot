from apscheduler.schedulers.blocking import BlockingScheduler

from mareabot import startup_bot

sched = BlockingScheduler()


@sched.scheduled_job("interval", minutes=7)
def timed_job():
    startup_bot()


sched.start()
