#!/usr/bin/env python
from distutils.core import setup

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name	= 'Pimoroni-PiGlow',
version 	= '1.0.1',
author        	= 'Philip Howard',
author_email	= 'phil@pimoroni.com',
description	= 'A module to control the PiGlow Raspberry Pi Addon Board',
long_description= 'A module to control the PiGlow Raspberry Pi Addon Board',
license	        = 'MIT',
keywords	= 'Raspberry Pi PiGlow',
url	        = 'http://www.pimoroni.com',
classifiers     = classifiers,
py_modules	= ['piglow'],
install_requires= ['sn3218','rpi.gpio >= 0.5.4']
)
