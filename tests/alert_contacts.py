#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import unittest
from uuid import uuid4
from upytimerobot import UptimeRobot


class URTestAlertContacts(unittest.TestCase):
    new_contact = {}

    @classmethod
    def setUp(cls):
        cls.uptr = UptimeRobot()

    def test_001_add_alert_contacts(self):
        new_ac = self.uptr.add_alert_contact('Unit Test', 2, 'unittest@example.com')
        self.assertIsNotNone(new_ac)
        self.assertIsNotNone(new_ac['stat'])
        self.assertEqual(new_ac['stat'], 'ok')
        self.__class__.new_contact = new_ac['alertcontact']

    def test_002_get_alert_contacts(self):
        contacts = self.uptr.get_alert_contacts()
        self.assertIsNotNone(contacts)
        self.assertIsNotNone(contacts['stat'])
        self.assertIn(str(self.__class__.new_contact['id']),
                      [x for v in contacts['alert_contacts'] for x in v.values()])

    def test_003_get_alert_contacts_nonexistent(self):
        contacts = self.uptr.get_alert_contacts(alert_contacts='123456')
        self.assertIsNotNone(contacts)
        self.assertIsNotNone(contacts['stat'])
        self.assertEqual(contacts['stat'], 'fail')
        self.assertEqual(contacts['error']['type'], 'not_found')

    def test_004_delete_alert_contacts(self):
        del_ac = self.uptr.delete_alert_contact(self.__class__.new_contact['id'])
        contacts = self.uptr.get_alert_contacts()
        self.assertIsNotNone(del_ac)
        self.assertIsNotNone(del_ac['stat'])
        self.assertEqual(del_ac['stat'], 'ok')
        self.assertNotIn(str(self.__class__.new_contact['id']),
                         [x for v in contacts['alert_contacts'] for x in v.values()])
