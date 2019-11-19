#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

from unittest import TestCase
from upytimerobot import UptimeRobot, colors


class URTestBase(TestCase):

    @classmethod
    def setUp(cls):
        cls.uptr = UptimeRobot()

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

    def test_003_colors(self):
        self.assertEqual(colors.red('text'), '\x1b[31mtext\x1b[0m')
        self.assertEqual(colors.green('text'), '\x1b[32mtext\x1b[0m')
        self.assertEqual(colors.yellow('text'), '\x1b[33mtext\x1b[0m')
        self.assertEqual(colors.blue('text'), '\x1b[34mtext\x1b[0m')
        self.assertEqual(colors.reset(), '\x1b[0m')

