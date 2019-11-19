#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import unittest
from tests import base, alert_contacts, monitors, mwindows, psps

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromTestCase(base.URTestBase))
suite.addTests(loader.loadTestsFromTestCase(alert_contacts.URTestAlertContacts))
suite.addTests(loader.loadTestsFromTestCase(monitors.URTestMonitors))
suite.addTests(loader.loadTestsFromTestCase(mwindows.URTestMWindows))
suite.addTests(loader.loadTestsFromTestCase(psps.URTestPSPS))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
