#!/bin/bash

apt-get update

apt-get install -y build-essential python-dev python-pip git
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
