#!/usr/bin/envpython3
# -*- coding: utf-8 -*-
#

import unittest
from upytimerobot import UptimeRobot


class UpytimeRobotTest(unittest.TestCase):

    def setUp(self):
        self.uptr = UptimeRobot()

    def test_aquire_account_info(self):
        account_info = self.uptr.get_account_details()
        self.assertIsNotNone(account_info)
        self.assertIsNotNone(account_info['stat'])

    def test_get_monitors(self):
        monitors = self.uptr.get_monitors()
        # print(monitors)
        self.assertIsNotNone(monitors)
        self.assertIsNotNone(monitors['stat'])

    def test_get_monitors_by_name(self):
        monitor = self.uptr.get_monitor_by_name('thinkit.net.br')
        # print(monitor)
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])

    def test_get_monitors_by_id(self):
        monitor = self.uptr.get_monitor_by_id('780661249')
        # print(monitor)
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])

    def test_get_monitors_by_status(self):
        monitor = self.uptr.get_monitor_by_status(2)
        # print(monitor)
        self.assertIsNotNone(monitor)

    def test_get_monitors_by_type(self):
        monitor = self.uptr.get_monitor_by_type(3)
        # print(monitor)
        self.assertIsNotNone(monitor)

    def test_get_alert_contacts(self):
        contacts = self.uptr.get_alert_contacts()
        # print(contacts)
        self.assertIsNotNone(contacts)
        self.assertIsNotNone(contacts['stat'])

    def test_get_mwindows(self):
        mwindow = self.uptr.get_mwindows()
        # print(mwindow)
        self.assertIsNotNone(mwindow)
        self.assertIsNotNone(mwindow['stat'])

    def test_get_psps(self):
        psp = self.uptr.get_psps()
        # print(psp)
        self.assertIsNotNone(psp)
        self.assertIsNotNone(psp['stat'])


if __name__ == '__main__':
    unittest.main()
    print("Passed through all the tests...")
