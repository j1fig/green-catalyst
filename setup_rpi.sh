#!/bin/bash

apt-get update

apt-get install -y build-essential python-dev python-pip git rabbitmq-server
pip install virtualenv

# virtenv setup
virtualenv .gc
source .gc/bin/activate

# pigpio install
wget abyz.co.uk/rpi/pigpio/pigpio.zip
unzip pigpio.zip
cd PIGPIO
make
make install
cd ..
rm -rf PIGPIO

# rabbitmq setup
rabbitmqctl add_user greencatalyst green
rabbitmqctl add_vhost vhost
rabbitmqctl set_permissions -p vhost greencatalyst ".*" ".*" ".*"
