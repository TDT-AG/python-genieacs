# python-genieacs

A Python API to interact with the [GenieACS](https://github.com/zaidka/genieacs) [REST API](https://github.com/zaidka/genieacs/wiki/API-Reference), but with the easiness and comfort of Python.

### Requirements

* Python 2 or 3
* [Requests](http://python-requests.org/)

### Usage

Take a look at *example.py*.

### License

This software is released under the terms of the
GNU General Public License v2:

[http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt](http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt)

### Todos

* high level abstracting methods for comfortable usage of the API
* user-definable error/exception handling (stop on error or warn and continue)
* setup.py

The following list contains all possible interactions with the GenieACS REST API. Interactions already implemented are enclosed in brackets.

#### Query GenieACS database:

* (list IDs of all devices)
* (search for devices:)
  * (by ID)
  * (by MAC)
* (list parameters for a given device)

#### Manage devices:

* (delete a given device from the database)

#### Manage tasks:

* (list all tasks)
  * (filtered by device)
* (create a task for a given device)
  * (refreshObject)
  * (setParameterValues)
  * (getParameterValues)
  * (addObject)
  * (reboot)
  * (factoryReset)
  * (download)
* (retry a faulty task at the next inform)
* (delete a given task)

#### Manage tags:

* (list tags filtered by device)
* (assign a tag to a device)
* (remove a tag from a device)

#### Manage presets:

* (list all presets)
* (write all presets to a file)
* (create or update a preset)
* (create all presets from a file)
* (delete a preset)

#### Manage objects:

* (list all objects)
* (write all objects to a file)
* (create or update an object)
* (create all objects from a file)
* (delete an object)

#### Manage provisions:

* (list all provisions)
* (write all provisions to a file)
* (create or update a provision)
* (create all provisions from a file)
* (delete a provision)

#### Manage files:

* (list all files)
* (list data of one or more specific files)
* (upload or overwrite a file)
* (delete an uploaded file)

#### Manage faults:

* (list IDs of all faults)
* (list all faults)
  * (filtered by device)
* (delete a given fault)
