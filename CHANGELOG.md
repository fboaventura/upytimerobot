# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
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

## WIP:[0.3.0] - TBD
This release will see all the remaining `Add` features.  Also I've already added the `coverage` and `unittests` support, preparing to have the release and publishing of the module on the CI/CD workflow.

__**Added**__
  - Unittests to make sure everything is working properly
  - Coverage verification
 
__**Changed**__
  - Init config was changed to support getting the API KEY, and other settings, through Class Call or Environment variables.
  - Renamed `README.rst` to [README.md](README.md)
  - Cosmetics improvements on the project `setup.py`, also on [CHANGELOG.md](CHANGELOG.md) and [README.md](README.md) files.

## [0.2.1] - 2018-06-28
Some work was made toward improving the collection of monitors by type, status, etc..

__**Added**__
  - `.add_monitor` to add new monitors
  - `.add_http_monitor` to add http/https monitors
  - `.add_ping_monitor` to add ping monitors
  - `.add_port_monitor` to add port monitors
  - File `add_monitor.py` to serve as example of what can be achieved 

__**Changed**__
  - `Changelog` texts to be more clear
  - FIX: `get_monitor_by_status` is now working properly
  - FIX: `get_monitor_by_type` is now working properly


## [0.1.0] - 2018-06-18
This is functional module already, one can query all the information regarding `account`, `monitors`, `alert contacts`, `maintenance windows` and `public status pages`.

Also, the functions are all well documented, containing all the possible parameters that can be used to each of the queries available.  

__**Added**__
  - Add `constants` file to hold parameters options and other constants that will be used

__**Changed**__
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

## 0.0.1 - 2018-06-15

The very beginning of this module, it arrives with all possible queries already done.  There are few documentation regarding the class and methods being implemented.
 
__**Added**__
  - Initial commit
  - Config file to host API key and other options
  - All read only API calls are implemented:
    - `getMonitors`
    - `getAccountDetails`
    - `getAlertContacts`
    - `getMWindows`
    - `getPSPs`


[0.3.0]: https://gitlab.com/fboaventura/upytimerobot/milestones/2
[0.2.1]: https://gitlab.com/fboaventura/upytimerobot/compare/0.1.0...0.2.1
[0.1.0]: https://gitlab.com/fboaventura/upytimerobot/compare/0.0.1...0.1.0
[Unreleased]: https://gitlab.com/fboaventura/upytimerobot/compare/0.2.1...master
