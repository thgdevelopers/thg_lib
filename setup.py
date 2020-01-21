#!/usr/bin/env python3
from __future__ import print_function

import glob
import os
import platform
import subprocess
import sys
import traceback
from distutils.command.install import INSTALL_SCHEMES
from distutils.sysconfig import get_python_inc
from distutils.util import convert_path

from setuptools import find_packages
from setuptools import setup

install_requires     = ['paramiko>=1.15.2',
                        'mako>=1.0.0',
                        'pyelftools>=0.2.4',
                        'capstone>=3.0.5rc2',
                        'ropgadget>=5.3',
                        'pyserial>=2.7',
                        'requests>=2.0',
                        'pip>=6.0.8',
                        'tox>=1.8.1',
                        'pygments>=2.0',
                        'pysocks',
                        'python-dateutil',
                        'packaging',
                        'psutil>=3.3.0',
                        'intervaltree>=3.0',
                        'sortedcontainers',
                        'unicorn',
			'distorm3'
]

# Check that the user has installed the Python development headers
PythonH = os.path.join(get_python_inc(), 'Python.h')
if not os.path.exists(PythonH):
    print("You must install the Python development headers!", file=sys.stderr)
    sys.exit(-1)

# Convert README.md to reStructuredText for PyPI
long_description = ''
try:
    long_description = subprocess.check_output(['pandoc', 'README.md', '--to=rst'], universal_newlines=True)
except Exception as e:
    print("Failed to convert README.md through pandoc, proceeding anyway", file=sys.stderr)
    traceback.print_exc()

setup(
    name                 = 'thg',
    python_requires      = '>=3.7',
    packages             = find_packages(),
    version              = '1.0.0dev',

    description          = "thg_lib - exploit lib for thg-interface",
    long_description     = long_description,
    author               = "darkcode0x00",
    author_email         = "darkcode357@gmail.com",
    url                  = 'futuro',
    download_url         = "dsa",
    install_requires     = install_requires,
    license              = "Mostly MIT, some BSD, see LICENSE",
    keywords             = 'thg_lib - exploit lib for thg-interface',
    classifiers          = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
        'Topic :: Software Development :: Assemblers',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Disassemblers',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: System Shells',
        'Topic :: Utilities',
    ]
)
