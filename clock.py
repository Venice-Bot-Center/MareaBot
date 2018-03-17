from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=20)
def timed_job():
    print('This job is run every three minutes.')


sched.start()
