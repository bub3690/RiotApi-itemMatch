#!/usr/bin/env python

import sys

from setuptools import setup, find_packages


install_requires = [
    "datapipelines",
    "merakicommons",
    "Pillow"
]

# Require python 3.6
if sys.version_info.major != 3 and sys.version_info.minor != 6:
    sys.exit("Cassiopeia requires Python 3.6.")

setup(
    name="cassiopeia",
    url="https://github.com/meraki-analytics/cassiopeia",
    description="Riot Games Developer API Wrapper (3rd Party)",
    keywords=["LoL", "League of Legends", "Riot Games", "API", "REST"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Real Time Strategy",
        "Topic :: Games/Entertainment :: Role-Playing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="MIT",
    packages=find_packages(),
    zip_safe=True,
    install_requires=install_requires,
    include_package_data=True
)