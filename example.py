#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Usage examples for python-genieacs

import genieacs

# Define GenieACS server and connect to it
genieacs.set_server("tr069.tdt.de", ssl=True, auth=True, user="tdt", passwd="tdt")
# refresh some device parameters
genieacs.task_refresh_object("000149-c1500-000149014AF8", "InternetGatewayDevice.DeviceInfo.")
# set a device parameter
genieacs.task_set_parameter_values("000149-c1500-000149014AF8", [["InternetGatewayDevice.BackupConfiguration.FileList", "backup.cfg"]])
# print all presets defined as a json object
genieacs.query_get_presets()
