#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import unittest
from uuid import uuid4
from upytimerobot import UptimeRobot


class UpytimeRobotTest(unittest.TestCase):
    new_contact = {}
    new_monitor = {}
    monitor_name = uuid4().__str__()

    def setUp(self):
        self.uptr = UptimeRobot()

    def test_000_acquire_account_info(self):
        account_info = self.uptr.get_account_details()
        self.assertIsNotNone(account_info)
        self.assertIsNotNone(account_info['stat'])
        self.assertEqual(account_info['stat'], 'ok')

    def test_001_add_monitor(self):
        monitor = self.uptr.add_monitor(self.__class__.monitor_name, 'https://lnx.frederico.cf', 1)
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'ok')
        self.__class__.new_monitor = monitor['monitor']

    def test_002_get_monitors(self):
        monitors = self.uptr.get_monitors()
        self.assertIsNotNone(monitors)
        self.assertIsNotNone(monitors['stat'])
        self.assertEqual(monitors['stat'], 'ok')
        self.assertIn(self.__class__.new_monitor['id'],
                      [x for v in monitors['monitors'] for x in v.values()])

    def test_003_get_monitors_by_name(self):
        monitor = self.uptr.get_monitor_by_name(self.__class__.monitor_name)
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'ok')
        self.assertEqual(monitor['monitors'][0]['id'], self.__class__.new_monitor['id'])

    def test_004_get_monitors_by_id(self):
        monitor = self.uptr.get_monitor_by_id(self.__class__.new_monitor['id'])
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'ok')
        self.assertEqual(monitor['monitors'][0]['friendly_name'], self.__class__.monitor_name)

    def test_005_get_monitors_by_status(self):
        monitor = self.uptr.get_monitor_by_status(2)
        self.assertIsNotNone(monitor)

    def test_006_get_monitors_by_type(self):
        monitor = self.uptr.get_monitor_by_type('1')
        self.assertIsNotNone(monitor)

    def test_007_delete_monitor(self):
        del_mon = self.uptr.delete_monitor(self.__class__.new_monitor['id'])
        monitors = self.uptr.get_monitors()
        self.assertIsNotNone(del_mon)
        self.assertIsNotNone(del_mon['stat'])
        self.assertEqual(del_mon['stat'], 'ok')
        self.assertNotIn(str(self.__class__.new_monitor['id']),
                         [x for v in monitors['monitors'] for x in v.values()])

    def test_008_add_alert_contacts(self):
        new_ac = self.uptr.add_alert_contact('Unit Test', 2, 'unittest@example.com')
        self.assertIsNotNone(new_ac)
        self.assertIsNotNone(new_ac['stat'])
        self.assertEqual(new_ac['stat'], 'ok')
        self.__class__.new_contact = new_ac['alertcontact']

    def test_009_get_alert_contacts(self):
        contacts = self.uptr.get_alert_contacts()
        self.assertIsNotNone(contacts)
        self.assertIsNotNone(contacts['stat'])
        self.assertIn(str(self.__class__.new_contact['id']),
                      [x for v in contacts['alert_contacts'] for x in v.values()])

    def test_010_delete_alert_contacts(self):
        del_ac = self.uptr.delete_alert_contact(self.__class__.new_contact['id'])
        contacts = self.uptr.get_alert_contacts()
        self.assertIsNotNone(del_ac)
        self.assertIsNotNone(del_ac['stat'])
        self.assertEqual(del_ac['stat'], 'ok')
        self.assertNotIn(str(self.__class__.new_contact['id']),
                         [x for v in contacts['alert_contacts'] for x in v.values()])

    def test_011_get_mwindows(self):
        mwindow = self.uptr.get_mwindows()
        self.assertIsNotNone(mwindow)
        self.assertIsNotNone(mwindow['stat'])
        self.assertEqual(mwindow['stat'], 'ok')

    def test_012_get_psps(self):
        psp = self.uptr.get_psps()
        self.assertIsNotNone(psp)
        self.assertIsNotNone(psp['stat'])
        self.assertEqual(psp['stat'], 'ok')


if __name__ == '__main__':
    unittest.main(verbosity=2)
