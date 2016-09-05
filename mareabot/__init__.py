from mareabot.api.task import set_task
from mareabot.app import app

if __name__ == '__main__':
    set_task()
    app.logger.info('Start thre app')
    app.run()
