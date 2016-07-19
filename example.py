#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Usage examples for python-genieacs

import genieacs

# Create a Connection object to interact with a GenieACS server
acs = genieacs.Connection("tr069.tdt.de", ssl=True, auth=True, user="tdt", passwd="tdt")
# refresh some device parameters
acs.task_refresh_object("000149-c1500-000149014AF8", "InternetGatewayDevice.DeviceInfo.")
# set a device parameter
acs.task_set_parameter_values("000149-c1500-000149014AF8", [["InternetGatewayDevice.BackupConfiguration.FileList", "backup.cfg"]])
# print all existing presets as a json object
acs.preset_get_all()
# create a new preset
acs.preset_put("Tagging", r'{ "weight": 0, "precondition": "{\"_tags\":{\"$ne\":\"tagged\"}}", "configurations": [ { "type": "add_tag", "tag":"tagged" }] }')
# delete the device from the database
acs.device_delete("000149-c1500-000149014AF8")
