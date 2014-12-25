from datetime import timedelta

from celery.task import periodic_task

from probe import Probe


sensor = Probe()


@periodic_task(run_every=timedelta(seconds=3))
def periodic_reading():
    sensor.report()
