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

* ensure python 2 and 3 compatibility
* setup.py

The following list contains all possible interactions with the GenieACS REST API. Interactions already implemented are enclosed in brackets.

#### Query GenieACS database:

* search for devices:
  * by ID
  * by MAC
* list parameters for a given device
* list tasks:
  * filtered by device
* (list presets)
* list files

#### Manage tasks:

* create a task for a given device
  * (refreshObject)
  * (setParameterValues)
  * getParameterValues
  * addObject
  * reboot
  * factoryReset
  * download
* retry a faulty task at the next inform
* delete a given task

#### Manage tags:

* assign a tag to a device
* remove a tag from a device

#### Manage presets:

* create or update a preset
* delete a preset

#### Manage files:

* upload or overwrite a file
* delete an uploaded file
* get one or all uploaded files
