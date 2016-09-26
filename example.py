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
# get a device parameter
acs.task_get_parameter_values("000149-c1500-000149014AF8", [["InternetGatewayDevice.BackupConfiguration.FileList"]])
# factory reset a device
acs.task_factory_reset("000149-c1500-000149014AF8")
# reboot a device
acs.task_reboot("000149-c1500-000149014AF8")
# add an object to a device
acs.task_add_object("000149-Kananga-P15", "VPNObject", [["InternetGatewayDevice.X_TDT-DE_OpenVPN"]])
# download a file
acs.task_download("000149-Kananga-P15", "9823de165bb983f24f782951", "Firmware.img")
# retry a faulty task
acs.task_retry("9h4769svl789kjf984ll")


# print all tasks of a given device
print(acs.task_get_all("000149-Kananga-P15"))
# search a device by its ID and print all corresponding data
print(acs.device_get_by_id("000149-Kananga-P15"))
# search a device by its MAC address and print all corresponding data
print(acs.device_get_by_MAC("00:01:49:ff:0f:01"))
# print 2 given parameters of a given device
print(acs.device_get_parameters("000149-Kananga-P15", "InternetGatewayDevice.DeviceInfo.SoftwareVersion,InternetGatewayDevice.X_TDT-DE_Interface.2.ProtoStatic.Ipv4.Address"))
# delete a task
acs.task_delete("9h4769svl789kjf984ll")


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

# assign a tag to a device
acs.tag_assign("000149-Kananga-P15", "tagged")
# remove a tag from a device
acs.tag_remove("000149-Kananga-P15", "tagged")

# print all existing files in the database
print(acs.file_get_all())
# delete a file from the database
acs.file_delete("Firmware.img")

# delete the device from the database
acs.device_delete("000149-c1500-000149014AF8")
