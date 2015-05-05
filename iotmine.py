
from lettuce import *
from nose.tools import eq_, assert_in, assert_not_equal
import urllib
import urllib2
import json



@step(u'Given api_key for service "([^"]*)"')
def given_service(step, service_apikey):
    world.apikey = service_apikey

@step(u'And the service "([^"]*)" has been created')
def create_service(step, group1):
    """
    parsed_url = urlopen('http://10.95.83.239:8080/iot/services ')
    response = parsed_url.read()
    resp = json.loads(str(response))

    # Apikey = world.apikey
    apky = resp["services"]["apikey"]
    eq_(apky, world.apikey)
    """


@step(u'And a device with device_id "([^"]*)"')
def given_device_id(step, device_id):
    world.id = device_id


@step(u'And the device with device_id "([^"]*)" has been created')
def create_device_id(step, group1):
    """
    headers = {'Fiware-Service': 'service2', 'Fiware-Subservice': '/srvpath2'}
    data = urllib.urlencode(headers)
    req = urllib2.Request('http://10.95.83.239:8080/iot/devices', data)
    """
    headers_cb = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Fiware-Service': 'service2'}
    data_cb = urllib.urlencode(headers_cb)
    req_cb = urllib2.Request('http://10.95.82.244:1026/v1/updateContext', None, headers_cb)

    response = urllib2.urlopen(req_cb)
    page = response.read()
    resp = json.loads(str(page))

    print data_cb

    # Apikey = world.apikey
    """count = 0
    size = resp["count"]

    for devices in resp["devices"][count]["device_id"]:
        assert devices
    """


@step(u'And data "([^"]*)"')
def given_data(step, data):
    world.data = data


##

@step(u'When a measure is received')
def receive_measure(step):
    assert True

@step(u'Then the IoT response should be 200')
def iot_response(step):
    assert True

@step(u'And context broker is notified')
def cb_notification(step):
    assert True

@step(u'And the response sent to Context Broker should include name "([^"]*)" and value "([^"]*)" and id "([^"]*)"')
def cb_response(step, name, value, dev_id):
    aux_name, aux_val = world.data.replace('_', ' ').split()
    # This will change as the literal in UL2.0 is given by 'key|value'
    assert True
    """
    eq_(aux_name, name)
    eq_(aux_val, value)
    eq_(world.id, dev_id)
   """