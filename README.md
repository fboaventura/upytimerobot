Uptime Robot integration for Python
============
Python3 module to interact with UptimeRobot API

Installation
------------
To get the latest stable release from PyPi

```(bash)
$ pip install upytimerobot
```

To get the latest commit from GitLab

```(bash
$ pip install -e git+git://gitlab.com/fboaventura/upytimerobot.git#egg=uptimerobot
```

Usage
-----
Use with Python:

```(python)
>>> from upytimerobot import UptimeRobot
>>> up = UptimeRobot(api_key=UPTIME_ROBOT_API_KEY)
>>> up.get_monitors()
{'stat': 'ok', 'pagination': {'offset': 0, 'limit': 1, 'total': 4}, 'monitors': [{'id': 90909090, 'friendly_name': 'my_monitor', 'url': '127.0.0.1', 'type': 3, 'sub_type': '', 'keyword_type': '', 'keyword_value': '', 'http_username': '', 'http_password': '', 'port': '', 'interval': 300, 'status': 2, 'ssl': {'brand': '', 'product': None, 'expires': 0}, 'create_datetime': 1480809958}]}

```


History
-------

latest

## 0.0.1 - 2018-06-15
### Added
- Initial commit
- Config file to host API key and other options
- All read only API calls are implemented:
  - getMonitors => `.get_monitors()`
  - getAccountDetails => `.get_account_details()`
  - getAlertContacts => `.get_alert_contacts()`
  - getMWindows => `.get_mwindows()`
  - getPSPs => `.get_pdpd()`


About the API
-------------

The full API is documented here: https://uptimerobot.com/api
