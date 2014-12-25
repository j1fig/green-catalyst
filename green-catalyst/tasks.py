from datetime import timedelta

from celery.task import periodic_task
from celery import Celery

from probe import Probe


app = Celery('tasks')
app.config_from_object('settings')

sensor = Probe()


@periodic_task(run_every=timedelta(seconds=3))
def periodic_reading():
    sensor.report()
