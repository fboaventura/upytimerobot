#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

from unittest import TestCase
from upytimerobot import UptimeRobot, colors


class URTestMWindows(TestCase):

    @classmethod
    def setUp(cls):
        cls.uptr = UptimeRobot()

    def test_001_get_mwindows(self):
        mwindow = self.uptr.get_mwindows()
        self.assertIsNotNone(mwindow)
        self.assertIsNotNone(mwindow['stat'])
        self.assertEqual(mwindow['stat'], 'ok')
