import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


def reading_json():
    pass
    #TODO Here code for reading the api

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=reading_json,
    trigger=IntervalTrigger(seconds=5),
    id='printing_job',
    name='Print date and time every five seconds',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

