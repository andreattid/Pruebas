from lettuce import *
from nose.tools import eq_, assert_in
import urllib
import urllib2
import requests
import json
import yaml
import string

"""******************************************************


        SET OF STEPS IN SCENARIO OUTLINE @4
                  TESTING SCENARIO
                  OTHER FUNCTIONS


*******************************************************"""


@step(u'Given a test')
def given_test(step):
    data = 'kdjaJdkasjd'

    for item in data:

        print item



def security(string):
    bool = 1
    for item in string:
        # Forbidden characters in ASCII (as they belong to the url
        if ord(item) < 32:
            bool = 0
        elif ord(item) == 38:
            bool = 0
        elif ord(item) == 124:
            bool = 0

        # Invalid characters in JSON. How can I improve this??
        elif ord(item) == 92:
            bool = 0
    return bool



"""******************************************************


        SET OF STEPS IN SCENARIO OUTLINE @1


*******************************************************"""





@step(u'api_key for service "([^"]*)" and device_id "([^"]*)" and data values')
def given_service(step, service_apikey, device_id):
    world.apikey = service_apikey
    world.id = device_id

    world.datas = []
    world.values = []
    world.size = len(step.hashes) - 1


    for item in step.hashes:
        # Security function to sketch a dataset and remove the items where a forbidden symbol appears
        # If wrong char appears in name, it will not be appended, and neither the value
        if security(item["name"]):
            world.datas.append(item["name"])
            if security(item["value"]):
                    world.values.append(item["value"])
            else:
                print "The value "+item["value"]+" cannot be appended"
        else:
            print "The name "+item["name"]+" cannot be appended"






@step(u'the service has been created')
def create_service(step):
    url = 'http://192.168.22.137:8085/iot/services'
    headers = {'Fiware-Service': 'A001', 'Fiware-Subservice': '/TestA001'}
    req = requests.get(url=url, headers=headers, data=None)
    text = req.text
    resp = json.loads(str(text))
    services = resp["services"]

    for service in services:
        eq_(service["apikey"], world.apikey, 'No service matching a current service')
        return


@step(u'a measure is sent to IoT Agent using GET')
def send_measure1(step):

    for i in range(0, world.size):
        data = world.datas[i]+'|'+world.values[i]
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
    world.req = req
    status = req.status_code
    eq_(status, 200)

    world.resp = yaml.safe_load(req.content)
    print world.resp

@step(u'the response sent to Context Broker should match with the data sent')
def cb_response(step):

    attributes = world.resp["contextElement"]["attributes"]

    for attribute in attributes:
        if attribute["name"] == world.datas[0]:
            eq_(attribute["name"], world.datas[0])
            eq_(attribute["value"], world.values[0])


@step(u'And the response sent to Context Broker should be invalid')
def invalid_resp(step):
    with open('filename.txt','w') as fout:
        fout.write(world.req.text)




"""
@step(u'the device has been created')
I decided to remove this step since I haven't figured out yet how to match a device created by
default with a device manually provided

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




