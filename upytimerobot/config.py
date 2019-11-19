#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
"""
Helper library for configuration handling
"""

# Imports
import configparser
import os
import sys

conf = configparser.ConfigParser()


def init(config_file='config.ini', config_section='default'):
    """
    Initialize the configuration file handling
    :param config_file: File that will be used to consult the configurations
    :param config_section: Profile to be used
    """
    config_open(config_file)


def config_write(config_file):
    """
    Write configuration into file

    :param config_file:
    """
    conf.write(open(config_file, 'w'))


def error_exit(error_message: str = "Oops! There was an error...", error_code: int = 1):
    """
    Exit with error message

    :param error_message: message to be shown on exit
    :param error_code: code to be used
    :return:
    """
    print('{}\n'.format(error_message))
    sys.exit(error_code)


def new_config(config_file, config_section='default', **kwargs):
    """
    Get data for new configuration file
    :param config_file:
    :param config_section:
    """

    if config_section is not 'default':
        conf['default'] = {}
        conf['default']['profile'] = config_section

    conf[config_section] = {}

    if 'api_key' in kwargs:
        conf[config_section]['api_key'] = kwargs['api_key']
        conf[config_section]['output'] = kwargs['output'] if 'output' in kwargs else 'json'
        conf[config_section]['logs'] = kwargs['logs'] if 'logs' in kwargs else 0
        conf[config_section]['alert_contacts'] = kwargs['alert_contacts'] if 'alert_contacts' in kwargs else ''
    else:
        conf[config_section]['api_key'] = str(input("Enter your UptimeRobot API Key: ") or
                                              error_exit('Missing API Key!'))
        conf[config_section]['output'] = str(input("Which is your favourite output format (json, xml or pretty)? [json]")
                                             or 'json')
        conf[config_section]['logs'] = str(input("Want to see logs by default (1: Yes or 0: No)? [0] ")
                                           or 0)

    config_write(config_file)


def config_open(config_file, config_section='default'):
    """
    Read configuration file
    :param config_file:
    :param config_section:
    :return:
    """
    if not os.path.exists(config_file):
        new_config(config_file, config_section)

    cfg = conf.read(config_file)

    return cfg
