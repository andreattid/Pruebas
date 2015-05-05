from lettuce import *
from nose.tools import eq_
import urllib
import urllib2
import requests
import json


@step(u'Given a test')
def given_test(step):
    url = 'http://10.95.82.244:1026/v1/contextEntities/type/thing/id/device_id1'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Fiware-Service': 'service2'}
    req = requests.get(url=url, headers=headers, data=None)
    text = req.text
    resp = json.loads(str(text))

    for attributes in resp["contextElement"]["attributes"]:

        print attributes







@step(u'Given api_key for service "([^"]*)"')
def given_service(step, service_apikey):
    world.apikey = service_apikey

@step(u'And the service "([^"]*)" has been created')
def create_service(step, group1):
    # Coger el GET que devuelve los servicios y buscar en el json el world.apikey

    url = 'http://10.95.83.239:8080/iot/services'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Fiware-Service': 'service2'}
    req = requests.get(url=url, headers=headers, data=None)
    text = req.text
    resp = json.loads(str(text))
    apky = resp["services"]["apikey"]
    eq_(apky, world.apikey)

@step(u'And a device with device_id "([^"]*)"')
def given_device_id(step, device_id):
    world.id = device_id

@step(u'And the device with device_id "([^"]*)" has been created')
def create_device_id(step, group1):
    # Buscar en el JSON si se ha creado un device similar al solicitado

    url = 'http://10.95.83.239:8080/iot/devices'
    headers = {'Fiware-Service': 'service2', 'Fiware-Subservice': '/srvpath2'}
    req = requests.get(url=url, headers=headers, data=None)
    resp = json.loads(str(req))

    count = 0
    size = resp["count"]

    # Esto lleva un loop porque los devices devueltos van en un array, y necesito contabilizarlos para recorrerlo
    ##HAY QUE ACABARLO PORQUE NO SE HACERLO SIN SEGUIR PROBANDO
    for device in resp["devices"][count]["device_id"]:
        if device != world.id:
            count = count + 1







@step(u'And data "([^"]*)"')
def given_data(step, data):
    world.data = data

@step(u'When a measure is received')
def receive_measure(step):
    # Comprobar que la medida se lanza desde dispo - GET y POST options
    assert True


@step(u'Then the IoT response should be 200')
def iot_response(step):
    assert True


@step(u'And context broker is notified')
def cb_notification(step):
    assert True


@step(u'And the response sent to Context Broker should include name "([^"]*)" and value "([^"]*)" and id "([^"]*)"')
def cb_response(step, name, value, dev_id):

    url = 'http://10.95.82.244:1026/v1/contextEntities/type/thing/id/device_id1'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Fiware-Service': 'service2'}
    req = requests.get(url=url, headers=headers, data=None)
    text = req.text
    resp = json.loads(str(text))

    aux_name = context
    eq_(aux_name, name)
    eq_(aux_val, value)
    eq_(world.id, dev_id)
