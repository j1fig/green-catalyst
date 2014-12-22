#!/bin/bash

apt-get update

apt-get install -y build-essential python-dev python-pip

pip install -r requirements.txt
