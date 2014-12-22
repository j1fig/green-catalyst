#!/bin/bash

apt-get update

apt-get install -y build-essential python-dev python-pip git

pip install virtualenv

virtualenv .gc
source .gc/env/bin/activate
