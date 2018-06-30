#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
"""
Small proof of concept script, to add new monitors using the upytimerobot module
"""
# Imports
import argparse
from upytimerobot import UptimeRobot


def main():
    options = argparse.ArgumentParser(
        description='Add new UptimeRobot monitor.',
        add_help=False
    )
    options.add_argument('--help', action='help', help='This help message')
    options.add_argument('--version', action='version', help='Show script version')
    options.add_argument('--name', '-n', nargs=1, type=str, action='store',
                         required=True, help='Friendly name of the monitor')
    options.add_argument('--url', '-u', nargs=1, type=str, action='store',
                         required=True, help='Url to be monitored')
    options.add_argument('--ping', '-i', action='store_true',
                         help='Add a ping monitor')
    options.add_argument('--http', '-h', action='store_true',
                         help='Add a HTTP(s) monitor')
    options.add_argument('--port', '-p', nargs=1, type=int, action='store',
                         help='Add a port monitor')
    opt = options.parse_args()

    ur = UptimeRobot()
    if opt.http:
        monitor = ur.add_http_monitor('{}'.format(opt.name[0]), '{}'.format(opt.url[0]))
    elif opt.port is not None:
        monitor = ur.add_port_monitor('{}'.format(opt.name[0]), '{}'.format(opt.url[0]),
                                      '{}'.format(int(opt.port[0])))
    else:
        monitor = ur.add_ping_monitor('{}'.format(opt.name[0]), '{}'.format(opt.url[0]))

    print(monitor)


# Main body
if __name__ == '__main__':
    main()
