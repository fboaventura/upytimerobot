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

    def test_001_get_request_status(self):
        self.assertEqual(self.uptr._get_request_status(200)['status_code'], 200)
        self.assertEqual(self.uptr._get_request_status(200)['stat'], 'ok')
        self.assertEqual(self.uptr._get_request_status(401)['status_code'], 401)
        self.assertEqual(self.uptr._get_request_status(401)['stat'], 'fail')
        self.assertEqual(self.uptr._get_request_status(403)['status_code'], 403)
        self.assertEqual(self.uptr._get_request_status(403)['stat'], 'fail')
        self.assertEqual(self.uptr._get_request_status(500)['status_code'], 500)
        self.assertEqual(self.uptr._get_request_status(500)['stat'], 'fail')
        self.assertEqual(self.uptr._get_request_status(404)['status_code'], 404)
        self.assertEqual(self.uptr._get_request_status(404)['stat'], 'fail')

    def test_002_error_message(self):
        error = self.uptr._error_messages('Oops', 200)
        self.assertEqual(error['code'], 200)
        self.assertEqual(error['message'], 'Oops')

    def test_003_add_monitor(self):
        monitor = self.uptr.add_monitor(self.__class__.monitor_name, 'https://lnx.frederico.cf', 1)
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'ok')
        self.__class__.new_monitor = monitor['monitor']

    def test_004_get_monitors(self):
        monitors = self.uptr.get_monitors()
        self.assertIsNotNone(monitors)
        self.assertIsNotNone(monitors['stat'])
        self.assertEqual(monitors['stat'], 'ok')
        self.assertIn(self.__class__.new_monitor['id'],
                      [x for v in monitors['monitors'] for x in v.values()])

    def test_005_get_monitors_by_name(self):
        monitor = self.uptr.get_monitor_by_name(self.__class__.monitor_name)
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'ok')
        self.assertEqual(monitor['monitors'][0]['id'], self.__class__.new_monitor['id'])

    def test_006_get_monitor_by_name_nonexistent(self):
        monitor = self.uptr.get_monitor_by_name('Not here')
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'ok')
        self.assertEqual(len(monitor['monitors']), 0)

    def test_007_get_monitors_by_id(self):
        monitor = self.uptr.get_monitor_by_id(self.__class__.new_monitor['id'])
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'ok')
        self.assertEqual(monitor['monitors'][0]['friendly_name'], self.__class__.monitor_name)

    def test_008_get_monitors_by_id_nonexistent(self):
        monitor = self.uptr.get_monitor_by_id('12345678')
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'fail')

    def test_009_get_monitors_by_status(self):
        monitor = self.uptr.get_monitor_by_status(2)
        self.assertIsNotNone(monitor)
        self.assertGreaterEqual(monitor.__len__(), 0)
        monitor = self.uptr.get_monitor_by_status(0)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'fail')
        self.assertEqual(monitor['message'], 'Monitor not found')

    def test_010_get_monitors_by_status_nonexistent(self):
        monitor = self.uptr.get_monitor_by_status(5)
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'fail')

    def test_011_get_monitors_by_type(self):
        monitor = self.uptr.get_monitor_by_type('1')
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'ok')

    def test_012_get_monitors_by_type_nonexistent(self):
        monitor = self.uptr.get_monitor_by_type('5')
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'fail')

    def test_013_delete_monitor(self):
        del_mon = self.uptr.delete_monitor(self.__class__.new_monitor['id'])
        monitors = self.uptr.get_monitors()
        self.assertIsNotNone(del_mon)
        self.assertIsNotNone(del_mon['stat'])
        self.assertEqual(del_mon['stat'], 'ok')
        self.assertNotIn(str(self.__class__.new_monitor['id']),
                         [x for v in monitors['monitors'] for x in v.values()])

    def test_014_add_alert_contacts(self):
        new_ac = self.uptr.add_alert_contact('Unit Test', 2, 'unittest@example.com')
        self.assertIsNotNone(new_ac)
        self.assertIsNotNone(new_ac['stat'])
        self.assertEqual(new_ac['stat'], 'ok')
        self.__class__.new_contact = new_ac['alertcontact']

    def test_015_get_alert_contacts(self):
        contacts = self.uptr.get_alert_contacts()
        self.assertIsNotNone(contacts)
        self.assertIsNotNone(contacts['stat'])
        self.assertIn(str(self.__class__.new_contact['id']),
                      [x for v in contacts['alert_contacts'] for x in v.values()])

    def test_016_get_alert_contacts_nonexistent(self):
        contacts = self.uptr.get_alert_contacts()
        self.assertIsNotNone(contacts)
        self.assertIsNotNone(contacts['stat'])
        self.assertIn(str(self.__class__.new_contact['id']),
                      [x for v in contacts['alert_contacts'] for x in v.values()])

    def test_017_delete_alert_contacts(self):
        del_ac = self.uptr.delete_alert_contact(self.__class__.new_contact['id'])
        contacts = self.uptr.get_alert_contacts()
        self.assertIsNotNone(del_ac)
        self.assertIsNotNone(del_ac['stat'])
        self.assertEqual(del_ac['stat'], 'ok')
        self.assertNotIn(str(self.__class__.new_contact['id']),
                         [x for v in contacts['alert_contacts'] for x in v.values()])

    def test_018_get_mwindows(self):
        mwindow = self.uptr.get_mwindows()
        self.assertIsNotNone(mwindow)
        self.assertIsNotNone(mwindow['stat'])
        self.assertEqual(mwindow['stat'], 'ok')

    def test_019_get_psps(self):
        psp = self.uptr.get_psps()
        self.assertIsNotNone(psp)
        self.assertIsNotNone(psp['stat'])
        self.assertEqual(psp['stat'], 'ok')


if __name__ == '__main__':
    unittest.main(verbosity=2)
