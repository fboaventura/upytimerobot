#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Python setup file for the upytimerobot app.

In order to register your app at pypi.python.org, create an account at
pypi.python.org and login, then register your new app like so:

    python setup.py register

If your name is still free, you can now make your first release but first you
should check if you are uploading the correct files:

    python setup.py sdist

Inspect the output thoroughly. There shouldn't be any temp files and if your
app includes staticfiles or templates, make sure that they appear in the list.
If something is wrong, you need to edit MANIFEST.in and run the command again.

If all looks good, you can make your first release:

    python setup.py sdist upload

For new releases, you need to bump the version number in
upytimerobot/__init__.py and re-run the above command.

For more information on creating source distributions, see
http://docs.python.org/2/distutils/sourcedist.html

"""
import os
from setuptools import setup, find_packages
import upytimerobot


def read(file_name):
    try:
        return open(os.path.join(os.path.dirname(__file__), file_name)).read()
    except IOError:
        return ''


setup(
    name="upytimerobot",
    description="""Module to interact with UptimeRobot API.""",
    version=upytimerobot.__version__,
    author=upytimerobot.__author__,
    author_email=upytimerobot.__email__,
    url=upytimerobot.__url__,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    license='MIT',
    platforms=['OS Independent'],
    keywords='uptime robot, api, monitoring, uptimerobot',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: DevOps",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Issues": "https://gitlab.com/fboaventura/upytimerobot/issues",
        "Changelog": "https://gitlab.com/fboaventura/upytimerobot/blob/master/CHANGELOG.md",
    }
)
