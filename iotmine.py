from lettuce import *
from nose.tools import eq_, assert_in
import urllib
import urllib2
import requests
import json


"""******************************************************


        SET OF STEPS IN SCENARIO OUTLINE @4
                  TESTING SCENARIO
                  OTHER FUNCTIONS


*******************************************************"""


@step(u'Given a test')
def given_test(step):
    url = 'http://192.168.22.137:8085/iot/d?i=dispo&d=t|8&k=abcabc'
    headers = {'Fiware-Service': 'A001', 'Fiware-Subservice': '/TestA001', 'Content-Type': 'application/json'}
    world.getresp = requests.get(url=url, headers=headers, data=None)




"""******************************************************


        SET OF STEPS IN SCENARIO OUTLINE @1


*******************************************************"""





@step(u'api_key for service "([^"]*)" and device_id "([^"]*)" and data values')
def given_service(step, service_apikey, device_id):
    world.apikey = service_apikey
    world.id = device_id
    data = step.hashes[0]["name"]
    value = step.hashes[0]["value"]

    i = 0
    world.datas = []
    world.values = []
    world.size = len(step.hashes)

    while i < world.size:
        world.datas.append(step.hashes[i]["name"])
        world.values.append(step.hashes[i]["value"])
        i = i+1



@step(u'the service has been created')
def create_service(step):
    url = 'http://192.168.22.137:8085/iot/services'
    headers = {'Fiware-Service': 'A001', 'Fiware-Subservice': '/TestA001'}
    req = requests.get(url=url, headers=headers, data=None)
    text = req.text
    resp = json.loads(str(text))
    services = resp["services"]

    for service in services:
        eq_(service["apikey"], world.apikey, 'El servicio solicitado no existe')
        return


@step(u'a measure is sent to IoT Agent using GET')
def send_measure1(step):
    data = world.datas[0]+'|'+world.values[0]
    url = 'http://192.168.22.137:8085/iot/d?i=' + world.id + '&d=' + data + '&k=' + world.apikey
    headers = {'Fiware-Service': 'A001', 'Fiware-Subservice': '/TestA001', 'Content-Type': 'application/json'}
    world.getresp = requests.get(url=url, headers=headers, data=None)


@step(u'a measure is sent to IoT Agent using POST')
def send_measure2(step):
    url = 'http://192.168.22.137:8085/iot/d?i=' + world.id + '&k=' + world.apikey
    headers = {'Fiware-Service': 'A001', 'Fiware-Subservice': '/TestA001', 'Content-Type': 'application/json'}

    i = 1
    data = world.datas[0]+'|'+world.values[0]

    while i < world.size:
        data = data+'#'+world.datas[i]+'|'+world.values[i]
        i = i+1

    world.postresp = requests.post(url=url, headers=headers, data=data)


@step(u'Then the IoT GET response should be 200')
def iot_get_response(step):
    eq_(world.getresp.status_code, 200)


@step(u'Then the IoT POST response should be 200')
def iot_post_response(step):
    eq_(world.postresp.status_code, 200)


@step(u'context broker is notified')
def cb_notification(step):
    url = 'http://10.95.82.244:1026/v1/contextEntities/type/thing/id/' + world.id
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Fiware-Service': 'A001',
               'Fiware-Subservice': '/TestA001'}
    req = requests.get(url=url, headers=headers, data=None)
    status = req.status_code
    eq_(status, 200)

    text = req.text
    world.resp = json.loads(str(text))


@step(u'the response sent to Context Broker should match with the data sent')
def cb_response(step):

    attributes = world.resp["contextElement"]["attributes"]

    for attribute in attributes:
        if attribute["name"] == world.datas[0]:
            eq_(attribute["name"], world.datas[0])
            eq_(attribute["value"], world.values[0])
    """


@step(u'the device has been created')
def create_device_id(step):
    url = 'http://192.168.22.137:8085/iot/devices'
    headers = {'Fiware-Service': 'service2', 'Fiware-Subservice': '/srvpath2'}
    req = requests.get(url=url, headers=headers, data=None)
    text = req.text
    resp = json.loads(str(text))
    devices = resp["devices"]

    for device in devices:
        if device["device_id"] == world.id:
            eq_(device["device_id"], world.id)

"""




