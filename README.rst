Python Module for Uptime Robot
==============================

Python3 module to interact with UptimeRobot API

Installation
------------

To get the latest stable release from PyPi

.. code:: bash

   $ pip install upytimerobot

To get the latest commit from GitLab

.. code:: bash

   $ pip install -e git+git://gitlab.com/fboaventura/upytimerobot.git#egg=uptimerobot

Usage
-----

Use with Python:

.. code:: python

   >>> from upytimerobot import UptimeRobot
   >>> up = UptimeRobot(api_key=UPTIME_ROBOT_API_KEY)
   >>> up.get_monitors()
   {'stat': 'ok', 'pagination': {'offset': 0, 'limit': 1, 'total': 4}, 'monitors': [{'id': 90909090, 'friendly_name': 'my_monitor', 'url': '127.0.0.1', 'type': 3, 'sub_type': '', 'keyword_type': '', 'keyword_value': '', 'http_username': '', 'http_password': '', 'port': '', 'interval': 300, 'status': 2, 'ssl': {'brand': '', 'product': None, 'expires': 0}, 'create_datetime': 1480809958}]}

ToDo
----
- Add support to edit existing Monitors
- Add support to delete existing Monitors
- Add support to add new Alert Contacts
- Add support to edit existing Alert Contacts
- Add support to delete existing Alert Contacts
- Add support to add new Maintenance Windows
- Add support to edit existing Maintenance Windows
- Add support to delete existing Maintenance Windows
- Add support to add new Public Status Pages
- Add support to edit existing Public Status Pages
- Add support to delete existing Public Status Pages
- Make the module work as a standalone script

History
-------

[0.2.1] - 2018-06-28
^^^^^^^^^^^^^^^^^^^^
Some work was made toward improving the collection of monitors by type, status, etc..

Added
"""""

- `.add_monitor` to add new monitors
- `.add_http_monitor` to add http/https monitors
- `.add_ping_monitor` to add ping monitors
- `.add_port_monitor` to add port monitors
- File `add_monitor.py` to serve as example of what can be achieved

Changed
"""""""

- `Changelog` texts to be more clear
- FIX: `get_monitor_by_status` is now working properly
- FIX: `get_monitor_by_type` is now working properly

[0.1.0] - 2018-06-18
^^^^^^^^^^^^^^^^^^^^

This is functional module already, one can query all the information regarding `account`, `monitors`, `alert contacts`, `maintenance windows` and `public status pages`.

Also, the functions are all well documented, containing all the possible parameters that can be used to each of the queries available.

Added
"""""

- Add `constants` file to hold parameters options and other constants that will be used

Changed
"""""""

- Renamed some internal usage methods to differentiate from the public ones
- Improved documentation on the existing methods
- The importing of some libraries
- `.get_monitors_by_name`: Changed validation if a monitor was recovered
- `.get_monitors_by_id`: Changed validation if a monitor was recovered
- Changed the name of the methods to a more pythonic naming:
    - `.getMonitors` -> `.get_monitors`
    - `.getAccountDetails` -> `.get_account_details`
    - `.getAlertContacts` -> `.get_alert_contacts`
    - `.getMWindows` -> `.get_mwindows`
    - `.getPSPs` -> `.get_psps`


About the API
-------------

The full API is documented here: https://uptimerobot.com/api
