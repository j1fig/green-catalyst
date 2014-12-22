from setuptools import setup
from setuptools import find_packages

import time
_version = '0.1.0.%s' % int(time.time())

_packages = find_packages(where='.')

install_requires = [
    'nose',
    'python-forecastio',
    'celery',
]

setup(
    name='green-catalyst',
    version=_version,
    description='An app to boost your plants',
    author='Joao Figueiredo',
    author_email='jfigueiredo@egoscape.net',
    url='log.egoscape.net',
    install_requires=install_requires,
    packages=_packages,
    include_package_data=True,
)
