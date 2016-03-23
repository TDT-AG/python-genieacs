# -*- coding: utf-8 -*-
#
# python-genieacs
# A Python API to interact with the GenieACS REST API
# https://github.com/TDT-GmbH/python-genieacs

import requests

# global variables
server_ip = ""
server_port = 7557
use_ssl = False
ssl_verify = False
use_auth = False
username = ""
password = ""
server_url = ""

base_url = ""
session = None

def __set_base_url():
    global base_url
    if not use_ssl:
        base_url = "http://"
    else:
        base_url = "https://"
    base_url += server_ip + ":" + str(server_port) + server_url

def __create_session():
    global session
    if session is not None:
        session.close()
    session = requests.Session()
    if use_auth:
        session.auth = (username, password)
    if use_ssl:
        session.verify = ssl_verify

def __request_post(url, data, conn_request=True):
    if conn_request:
        request_url = base_url + url + "?connection_request"
    else:
        request_url = base_url + url
    r = session.post(request_url, json=data)
    r.raise_for_status()

def set_server(ip, port=7557, ssl=False, verify=False, auth=False, user="", passwd="", url=""):
    global server_ip, server_port, use_ssl, ssl_verify, use_auth, username, password, server_url
    server_ip = ip
    server_port = port
    use_ssl = ssl
    ssl_verify = verify
    use_auth = auth
    username = user
    password = passwd
    server_url = url
    __set_base_url()
    __create_session()

def task_refresh_object(device, object_name, conn_request=True):
    data = { "name": "refreshObject",
             "objectName": object_name }
    __request_post("/devices/" + device + "/tasks", data, conn_request)

def task_set_parameter_values(device, parameter_values, conn_request=True):
    data = { "name": "setParameterValues",
             "parameterValues": parameter_values }
    __request_post("/devices/" + device + "/tasks", data, conn_request)

def query_get_presets():
    r = session.get(base_url + "/presets")
    r.raise_for_status()
    print(r.text)
