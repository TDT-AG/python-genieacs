#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Usage examples for python-genieacs

import genieacs

# set a device_id for the following methods
device_id = "000149-c1500-000149014AF8"

# Create a Connection object to interact with a GenieACS server
acs = genieacs.Connection("tr069.tdt.de", ssl=True, auth=True, user="tdt", passwd="tdt")

# refresh some device parameters
acs.task_refresh_object(device_id, "InternetGatewayDevice.DeviceInfo.")
# set a device parameter
acs.task_set_parameter_values(device_id, [["InternetGatewayDevice.BackupConfiguration.FileList", "backup.cfg"]])
# get a device parameter
acs.task_get_parameter_values(device_id, [["InternetGatewayDevice.BackupConfiguration.FileList"]])
# factory reset a device
acs.task_factory_reset(device_id)
# reboot a device
acs.task_reboot(device_id)
# add an object to a device
acs.task_add_object(device_id, "VPNObject", [["InternetGatewayDevice.X_TDT-DE_OpenVPN"]])
# download a file
acs.task_download(device_id, "9823de165bb983f24f782951", "Firmware.img")
# retry a faulty task
acs.task_retry("9h4769svl789kjf984ll")


# print all tasks of a given device
print(acs.task_get_all(device_id))
# print IDs of all devices
print(acs.device_get_all_IDs())
# search a device by its ID and print all corresponding data
print(acs.device_get_by_id(device_id))
# search a device by its MAC address and print all corresponding data
print(acs.device_get_by_MAC("00:01:49:ff:0f:01"))
# print the value of a given parameter of a given device
print(acs.device_get_parameter(device_id, "InternetGatewayDevice.DeviceInfo.SoftwareVersion"))
# print 2 given parameters of a given device
print(acs.device_get_parameters(device_id, "InternetGatewayDevice.DeviceInfo.SoftwareVersion,InternetGatewayDevice.X_TDT-DE_Interface.2.ProtoStatic.Ipv4.Address"))
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

# create a new provision
acs.provision_create("Logging", '// This is a comment\nlog("Hello World!");')
# write all existing provisions to a file and store them in a json object
provision_data = acs.provision_get_all('provisions.json')
# delete all provisisions
for provision in provision_data:
    acs.provision_delete(provision["_id"])
# create all provisions from the file
acs.provision_create_all_from_file('provisions.json')

# print all tags of a given device
print(acs.tag_get_all(device_id))
# assign a tag to a device
acs.tag_assign(device_id, "tagged")
# remove a tag from a device
acs.tag_remove(device_id, "tagged")

# print all existing files in the database
print(acs.file_get_all())
# print data of a specific file
print(str(acs.file_get(fileType="12 Other File", version="0.4")))
# upload a new or modified file
acs.file_upload("Firmware.img", "1 Firmware Upgrade Image", "123456", "r4500", "2.0")
# delete a file from the database
acs.file_delete("Firmware.img")

# delete the device from the database
acs.device_delete(device_id)
