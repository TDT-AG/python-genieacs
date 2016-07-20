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
# write all existing presets to a file and store them in an object
preset_data = acs.preset_get_all('presets.json')
# delete all presets
for preset in preset_data:
    acs.preset_delete(preset["_id"])
# create all presets from the file
acs.preset_create_all_from_file('presets.json')
# delete the device from the database
acs.device_delete("000149-c1500-000149014AF8")
