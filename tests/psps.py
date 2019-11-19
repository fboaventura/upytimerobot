#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

from unittest import TestCase
from upytimerobot import UptimeRobot, colors


class URTestPSPS(TestCase):

    @classmethod
    def setUp(cls):
        cls.uptr = UptimeRobot()

    def test_001_get_psps(self):
        psp = self.uptr.get_psps()
        self.assertIsNotNone(psp)
        self.assertIsNotNone(psp['stat'])
        self.assertEqual(psp['stat'], 'ok')
