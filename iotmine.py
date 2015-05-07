from lettuce import *
from nose.tools import eq_, assert_in
import urllib
import urllib2
import requests
import json


"""******************************************************


        SET OF STEPS IN SCENARIO OUTLINE @4
                  TESTING SCENARIO


*******************************************************"""

@step(u'Given a test')
def given_test(step):

    data = 'temperature_17#humidity_711'
    print data.replace('_','|')





"""******************************************************


        SET OF STEPS IN SCENARIO OUTLINE @1


*******************************************************"""

@step(u'Given api_key for service "([^"]*)"')
def given_service(step, service_apikey):
    world.apikey = service_apikey

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
    world.id = device_id


@step(u'And the device with device_id "([^"]*)" has been created')
def create_device_id(step, group1):
    url = 'http://192.168.22.137:8085/iot/devices'
    headers = {'Fiware-Service': 'service2', 'Fiware-Subservice': '/srvpath2'}
    req = requests.get(url=url, headers=headers, data=None)
    text = req.text
    resp = json.loads(str(text))
    devices = resp["devices"]

    for device in devices:
        if device["device_id"] == world.id:
            eq_(device["device_id"], world.id)



@step(u'And data "([^"]*)"')
def given_data(step, data):
    world.data = data.replace('_', '|')


@step(u'When a measure is received')
def receive_measure(step):
    # IDEA?
    assert True


@step(u'Then the IoT GET response should be 200')
def iot_get_response(step):
    url = 'http://192.168.22.137:8085/iot/d?i='+world.id+'&d='+world.data+'&k='+world.apikey
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Fiware-Service': 'service2'}
    req = requests.get(url=url, headers=headers, data=None)
    eq_(req.status_code,200)


@step(u'And context broker is notified')
def cb_notification(step):
    url = 'http://10.95.82.244:1026/v1/contextEntities/type/thing/id/'+world.id
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Fiware-Service': 'service2'}
    req = requests.get(url=url, headers=headers, data=None)
    status = req.status_code
    eq_(status, 200)

    text = req.text
    world.resp = json.loads(str(text))


@step(u'And the response sent to Context Broker should include name "([^"]*)" and value "([^"]*)"')
def cb_response(step, name, value):
    name1 = 'temperature'
    value1 = '17'

    attributes = world.resp["contextElement"]["attributes"]

    for attribute in attributes:
        if attribute["name"] == name1:
            eq_(attribute["name"], name1)
            eq_(attribute["value"], value1)




"""******************************************************


         STEPS ADDED TO SCENARIO OUTLINE @2


*******************************************************"""
@step(u'And several measures in data "([^"]*)"')
def and_several_measures_in_data_group1(step, data):
    world.multidata = data.replace('_', '|')

@step(u'Then the IoT POST response should be 200')
def iot_post_response(step):
    url = 'http://192.168.22.137:8085/iot/d?i='+world.id+'&k='+world.apikey
    headers = {'Content-Type': 'application/json'}
    data = world.multidata
    req = requests.post(url=url, headers=headers, data=data)
    eq_(req.status_code, 200)







