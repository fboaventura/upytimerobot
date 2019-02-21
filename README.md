![pipeline](https://gitlab.com/fboaventura/upytimerobot/badges/master/pipeline.svg)
![coverage](https://gitlab.com/fboaventura/upytimerobot/badges/master/coverage.svg?job=coverage)
[![codecov](https://codecov.io/gl/fboaventura/upytimerobot/branch/master/graph/badge.svg)](https://codecov.io/gl/fboaventura/upytimerobot)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/upytimerobot.svg)
![PyPI](https://img.shields.io/pypi/v/upytimerobot.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/upytimerobot.svg)
![PyPI - License](https://img.shields.io/pypi/l/upytimerobot.svg)
![snyk vulnerabilities](https://img.shields.io/snyk/vulnerabilities/github/fboaventura/upytimerobot.svg?style=flat)

# Python Module for Uptime Robot

Python3 module to interact with [UptimeRobot API]

## Installation

To get the latest stable release from PyPi

```(bash)
   $ pip install upytimerobot
```

To get the latest commit from GitLab

```(bash)
   $ pip install -e git+git://gitlab.com/fboaventura/upytimerobot.git#egg=uptimerobot
```

## Usage

Use with Python:

```python
   >>> from upytimerobot import UptimeRobot
   >>> up = UptimeRobot(api_key=UPTIME_ROBOT_API_KEY)
   >>> up.get_monitors()
   {'stat': 'ok', 'pagination': {'offset': 0, 'limit': 1, 'total': 4}, 'monitors': [{'id': 90909090, 'friendly_name': 'my_monitor', 'url': '127.0.0.1', 'type': 3, 'sub_type': '', 'keyword_type': '', 'keyword_value': '', 'http_username': '', 'http_password': '', 'port': '', 'interval': 300, 'status': 2, 'ssl': {'brand': '', 'product': None, 'expires': 0}, 'create_datetime': 1480809958}]}
```

## Configuration

On the first call of the class, if there is no ``config.ini`` file, you will be asked to provide the ``API KEY`` for your UptimeRobot account.

You may also use environment variables:

```bash   
    UPTIME_API="uXXXX-XXXX-XXXX"
    UPTIME_LOGS=[0|1]
    UPTIME_OUTPUT="[json|xml]"
    UPTIME_CONTACTS="[XXXX-XXXX-XXXX]"
```

or you may call the class passing the desired values:

```python
    >>> from upytimerobot import UptimeRobot
    >>> up = UptimeRobot(api_key="uXXXX-XXXX-XXXX",
                         output="json", output=0,
                         alert_contacts='XXXX-XXXX')
```

The default values for the above variables are:

```
    output = json
    logs = 0
    alert_contacts = ''
```

## ToDo

- Add support to edit existing Monitors (#1)
- Add support to add new Alert Contacts  (#2)
- Add support to add new Maintenance Windows (#3)
- Add support to add new Public Status Pages (#4)
- Add support to delete existing Monitors (#5)
- Add support to delete existing Maintenance Windows (#6)
- Add support to delete existing Public Status Pages (#7)
- Add support to edit existing Alert Contacts (#8)
- Add support to edit existing Maintenance Windows (#9)
- Add support to edit existing Public Status Pages (#10)
- Add support to delete existing Alert Contacts (#11)
- Make the module work as a standalone script

## Change Log

The actual Changelog and other code related modifications and comments can be seen at the [CHANGELOG.md]() file.

## About the API

The full API is documented here: [https://uptimerobot.com/api]()

[UptimeRobot API]: https://uptimerobot.com/api
