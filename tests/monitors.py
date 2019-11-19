#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

from unittest import TestCase
from uuid import uuid4
from upytimerobot import UptimeRobot


class URTestMonitors(TestCase):
    new_monitor = {}
    monitor_name = uuid4().__str__()

    @classmethod
    def setUp(cls):
        cls.uptr = UptimeRobot()

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

    def test_004_get_monitor_by_name_nonexistent(self):
        monitor = self.uptr.get_monitor_by_name('Not here')
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'ok')
        self.assertEqual(len(monitor['monitors']), 0)

    def test_005_get_monitors_by_id(self):
        monitor = self.uptr.get_monitor_by_id(self.__class__.new_monitor['id'])
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'ok')
        self.assertEqual(monitor['monitors'][0]['friendly_name'], self.__class__.monitor_name)

    def test_006_get_monitors_by_id_nonexistent(self):
        monitor = self.uptr.get_monitor_by_id('12345678')
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'fail')

    def test_007_get_monitors_by_status(self):
        monitor = self.uptr.get_monitor_by_status(2)
        self.assertIsNotNone(monitor)
        self.assertGreaterEqual(monitor.__len__(), 0)
        monitor = self.uptr.get_monitor_by_status(0)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'fail')
        self.assertEqual(monitor['message'], 'Monitor not found')

    def test_008_get_monitors_by_status_nonexistent(self):
        monitor = self.uptr.get_monitor_by_status(5)
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'fail')

    def test_009_get_monitors_by_type(self):
        monitor = self.uptr.get_monitor_by_type('1')
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'ok')

    def test_010_get_monitors_by_type_nonexistent(self):
        monitor = self.uptr.get_monitor_by_type('5')
        self.assertIsNotNone(monitor)
        self.assertIsNotNone(monitor['stat'])
        self.assertEqual(monitor['stat'], 'fail')

    def test_011_delete_monitor(self):
        del_mon = self.uptr.delete_monitor(self.__class__.new_monitor['id'])
        monitors = self.uptr.get_monitors()
        self.assertIsNotNone(del_mon)
        self.assertIsNotNone(del_mon['stat'])
        self.assertEqual(del_mon['stat'], 'ok')
        self.assertNotIn(str(self.__class__.new_monitor['id']),
                         [x for v in monitors['monitors'] for x in v.values()])
