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

# create a new preset
acs.preset_create("Tagging", r'{ "weight": 0, "precondition": "{\"_tags\":{\"$ne\":\"tagged\"}}", "configurations": [ { "type": "add_tag", "tag":"tagged" }] }')
# write all existing presets to a file and store them in a json object
preset_data = acs.preset_get_all('presets.json')
# delete all presets
for preset in preset_data:
    acs.preset_delete(preset["_id"])
# create all presets from the file
acs.preset_create_all_from_file('presets.json')

# create a new object
acs.object_create("CreatedObject", r'{"Param1": "Value1", "Param2": "Value2", "_keys":["Param1"]}')
# write all existing objects to a file and store them in a json object
object_data = acs.object_get_all('objects.json')
# delete all objects
for gobject in object_data:
    acs.object_delete(gobject["_id"])
# create all objects from the file
acs.object_create_all_from_file('objects.json')

# delete a file from the database
acs.file_delete("Test1")

# delete the device from the database
acs.device_delete("000149-c1500-000149014AF8")
