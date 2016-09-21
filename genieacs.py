# -*- coding: utf-8 -*-
#
# python-genieacs
# A Python API to interact with the GenieACS REST API
# https://github.com/TDT-GmbH/python-genieacs

import requests
import json

class Connection(object):
    """Connection object to interact with the GenieACS server."""
    def __init__(self, ip, port=7557, ssl=False, verify=False, auth=False, user="", passwd="", url=""):
        self.server_ip = ip
        self.server_port = port
        self.use_ssl = ssl
        self.ssl_verify = verify
        self.use_auth = auth
        self.username = user
        self.password = passwd
        self.server_url = url
        self.base_url = ""
        self.session = None
        self.__set_base_url()
        self.__create_session()

    def __del__(self):
        if self.session is not None:
            self.session.close()

    def __set_base_url(self):
        if not self.use_ssl:
            self.base_url = "http://"
        else:
            self.base_url = "https://"
        self.base_url += self.server_ip + ":" + str(self.server_port) + self.server_url

    def __create_session(self):
        if self.session is None:
            self.session = requests.Session()
            if self.use_auth:
                self.session.auth = (self.username, self.password)
            if self.use_ssl:
                self.session.verify = self.ssl_verify

    def __request_post(self, url, data, conn_request=True):
        if conn_request:
            request_url = self.base_url + url + "?connection_request"
        else:
            request_url = self.base_url + url
        r = self.session.post(request_url, json=data)
        r.raise_for_status()

    def __request_put(self, url, data):
        request_url = self.base_url + url
        r = self.session.put(request_url, data)
        r.raise_for_status()

    ##### methods for devices #####

    def device_delete(self, device_id):
        """Delete a given device from the database"""
        r = self.session.delete(self.base_url + "/devices/" + device_id)
        r.raise_for_status()

    ##### methods for tasks #####

    def task_refresh_object(self, device_id, object_name, conn_request=True):
        """Create a refreshObject task for a given device"""
        data = { "name": "refreshObject",
                 "objectName": object_name }
        self.__request_post("/devices/" + device_id + "/tasks", data, conn_request)

    def task_set_parameter_values(self, device_id, parameter_values, conn_request=True):
        """Create a setParameterValues task for a given device"""
        data = { "name": "setParameterValues",
                 "parameterValues": parameter_values }
        self.__request_post("/devices/" + device_id + "/tasks", data, conn_request)

    def task_get_parameter_values(self, device_id, parameter_names, conn_request = True):
        """Create a getParameterValues task for a given device"""
        data = { "name": "getParameterValues",
                "parameterNames": parameter_names}
        self.__request_post("/devices/" + device_id + "/tasks", data, conn_request)

    def task_add_object(self, device_id, object_name, object_path, conn_request=True):
        """Create an addObject task for a given device"""
        data = { "name": "addObject", object_name : object_path}
        self.__request_post("/devices/" + device_id + "/tasks", data, conn_request)

    def task_reboot(self, device_id, conn_request=True):
        """Create a reboot task for a given device"""
        data = { "name": "reboot"}
        self.__request_post("/devices/" + device_id + "/tasks", data, conn_request)

    def task_factory_reset(self, device_id, conn_request=True):
        """Create a factoryReset task for a given device"""
        data = { "name": "factoryReset"}
        self.__request_post("/devices/" + device_id + "/tasks", data, conn_request)

    def task_download(self, device_id, file_id, file_name, conn_request=True):
        """Create a download task for a given device"""
        data = { "name": "download", "file": file_id, "filename": file_name}
        self.__request_post("/devices/" + device_id + "/tasks", data, conn_request)

    def task_retry(self, task_id, conn_request=True):
        "Retry a faulty task at the next inform"
        r = self.session.post(self.base_url + "/tasks/" + task_id + "/retry")
        r.raise_for_status()

    def task_delete(self, task_id, conn_request=True):
        """Delete a Task for a given device"""
        # Warning: Error if task_id doesn't exist
        r = self.session.delete(self.base_url + "/tasks/" + task_id)
        r.raise_for_status()

    def task_get_all(self, device_id, filename = None, conn_request=True):
        """Create all tasks from a given device contained in a json file"""
        quoted_id = requests.utils.quote("{\"device\":\"" + device_id + "\"}", safe = '')
        r = self.session.get(self.base_url + "/tasks/" + "?query=" + quoted_id)
        r.raise_for_status()
        data = r.json()
        if filename is not None:
            f = open(filename, 'w')
            json.dump(data, f)
            f.close()
        return data



    ##### methods for tags ######

    def tag_assign(self, device_id, tag_name):
        """Assign a tag to a device"""
        self.__request_post("/devices/" + device_id + "/tags/" + tag_name, None, False)

    def tag_remove(self, device_id, tag_name):
        """Remove a tag from a device"""
        r = self.session.delete(self.base_url + "/devices/" + device_id + "/tags/" + tag_name)
        r.raise_for_status()


    ##### methods for presets #####

    def preset_create(self, preset_name, data):
        """Create a new preset or update a preset with a given name"""
        self.__request_put("/presets/" + preset_name, data)

    def preset_create_all_from_file(self, filename):
        """Create all presets contained in a json file"""
        f = open(filename, 'r')
        data = json.load(f)
        f.close()
        for preset in data:
            preset_name = preset["_id"]
            del preset["_id"]
            self.__request_put("/presets/" + preset_name, json.dumps(preset))

    def preset_get_all(self, filename=None):
        """Get all existing presets as a json object, optionally write them to a file"""
        r = self.session.get(self.base_url + "/presets")
        r.raise_for_status()
        data = r.json()
        if filename is not None:
            f = open(filename, 'w')
            json.dump(data, f)
            f.close()
        return data

    def preset_delete(self, preset_name):
        """Delete a given preset"""
        r = self.session.delete(self.base_url + "/presets/" + preset_name)
        r.raise_for_status()

    ##### methods for objects #####

    def object_create(self, object_name, data):
        """Create a new object or update an object with a given name"""
        self.__request_put("/objects/" + object_name, data)

    def object_create_all_from_file(self, filename):
        """Create all objects contained in a json file"""
        f = open(filename, 'r')
        data = json.load(f)
        f.close()
        for gobject in data:
            object_name = gobject["_id"]
            del gobject["_id"]
            self.__request_put("/objects/" + object_name, json.dumps(gobject))

    def object_get_all(self, filename=None):
        """Get all existing objects as a json object, optionally write them to a file"""
        r = self.session.get(self.base_url + "/objects")
        r.raise_for_status()
        data = r.json()
        if filename is not None:
            f = open(filename, 'w')
            json.dump(data, f)
            f.close()
        return data

    def object_delete(self, object_name):
        """Delete a given object"""
        r = self.session.delete(self.base_url + "/objects/" + object_name)
        r.raise_for_status()

    ##### methods for files #####

    def file_delete(self, filename):
        """Delete a given file"""
        r = self.session.delete(self.base_url + "/files/" + filename)
        r.raise_for_status()

    def file_get_all(self,  filename=None):
        """Get all files as a json object, optionally write them to a file"""
        r = self.session.get(self.base_url + "/files")
        r.raise_for_status()
        data = r.json()
        if filename is not None:
            f = open(filename, 'w')
            json.dump(data, f)
            f.close()
        return data
