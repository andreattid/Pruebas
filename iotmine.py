from lettuce import *
from nose.tools import eq_, assert_in
import urllib
import urllib2
import requests
import json


@step(u'Given a test')
def given_test(step):
    name = 'temperature'
    value = '17'
    print world.resp








@step(u'Given api_key for service "([^"]*)"')
def given_service(step, service_apikey):
    world.apikey = 'apikey3'

@step(u'And the service "([^"]*)" has been created')
def create_service(step, group1):

    url = 'http://192.168.22.137:8085/iot/services'
    headers = {'Fiware-Service': 'service2', 'Fiware-Subservice': '/srvpath2'}
    req = requests.get(url=url, headers=headers, data=None)
    text = req.text
    resp = json.loads(str(text))
    services = resp["services"]

    for service in services:
        eq_(service["apikey"], world.apikey, 'El servicio solicitado si existe')
        return

@step(u'And a device with device_id "([^"]*)"')
def given_device_id(step, device_id):
    world.id = 'device_id1'

@step(u'And the device with device_id "([^"]*)" has been created')
def create_device_id(step, group1):
    url = 'http://192.168.22.137:8085/iot/devices'
    headers = {'Fiware-Service': 'service2', 'Fiware-Subservice': '/srvpath2'}
    req = requests.get(url=url, headers=headers, data=None)
    text = req.text
    resp = json.loads(str(text))
    devices = resp["devices"]

    for device in devices:
        eq_(device["device_id"], world.id)
        return

@step(u'And data "([^"]*)"')
def given_data(step, data):
    world.data = data

@step(u'When a measure is received')
def receive_measure(step):
    # IDEA?
    assert True

@step(u'Then the IoT response should be 200')
def iot_response(step):
    url = 'http://192.168.22.137:8085/iot/d?i=device_id&d=att_name|15&k=apikey3'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Fiware-Service': 'service2'}
    req = requests.get(url=url, headers=headers, data=None)
    eq_(req.status_code,200)

@step(u'And context broker is notified')
def cb_notification(step):
    url = 'http://10.95.82.244:1026/v1/contextEntities/type/thing/id/device_id1'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Fiware-Service': 'service2'}
    req = requests.get(url=url, headers=headers, data=None)
    status = req.status_code
    eq_(status, 200)

    text = req.text
    world.resp = json.loads(str(text))

@step(u'And the response sent to Context Broker should include name "([^"]*)" and value "([^"]*)" and id "([^"]*)"')
def cb_response(step, name, value, dev_id):
    name1 = 'temperature'
    value1 = '17'
    
    attributes = world.resp["contextElement"]["attributes"]

    for attribute in attributes:
        if attribute["name"] == name:
            eq_(attribute["name"], name1)
            eq_(attribute["value"],value1)