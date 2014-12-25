from time import sleep

from pigpio import pi
from dht11driver import DHT11


class Probe(object):
    """
    A small wrapper class around DHT11 and pigpio drivers
    that reports info to a web server
    """
    def __enter__(self):
        class ProbeResource(object):
            def __init__(self):
                self.pi = pi()
                self.dht = DHT11(self.pi, 4, power=1)
                self.reading_number = 0

            def report(self):
                """
                Takes a reading and posts it to a web server in JSON
                """
                self.dht.trigger()
                sleep(0.2)
                self.reading_number += 1
                print("{} {} {} {:3.2f} {} {} {} {}".format(
                    self.reading_number, self.dht.humidity(),
                    self.dht.temperature(), self.dht.staleness(),
                    self.dht.bad_checksum(), self.dht.short_message(),
                    self.dht.missing_message(), self.dht.sensor_resets()))

            def release(self):
                self.dht.cancel()
                self.pi.stop()
        self.resource = ProbeResource()
        return self.resource

    def __exit__(self, type, value, traceback):
        self.dht.cancel()
        self.pi.stop()
