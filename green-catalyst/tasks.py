from time import sleep
from datetime import timedelta

from celery.task import periodic_task
from pigpio import pi
from dht11driver import DHT11


@periodic_task(run_every=timedelta(seconds=3))
def periodic_reading():
    pass
