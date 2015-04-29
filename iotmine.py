from lettuce import *

@step(u'a device with device_id "([^"]*)"')
def check_dev_id(step, flow_id):
    world.flow_id = flow_id

@step(u'data "([^"]*)"')
def check_data(step, flow_data):
    world.flow_data = flow_data.replace('_', '|')

@step(u'And api_key for service "([^"]*)"')
def check_apikey(step, flow_apikey):
    world.flow_apikey = flow_apikey

@step(u'a request is sent')
def sending_req(step):
    assert True

@step(u'the IoT response should be ')
def iot_resp(step):
    assert True

@step(u'the IoT body response should include id "([^"]*)" and type "([^"]*)"')
def body_shape1(step, iot_id, iot_type):
    assert world.flow_id == iot_id
    print(world.flow_id)
    print(iot_id)
    print step.hashes[0]

@step(u'the IoT body response for the attributes should include name "(\w+)" and value "(\w+)"')
def body_shape2(step, iot_name, iot_val):
    name, val = world.flow_data.replace('|', ' ').split()
    assert name == iot_name
    print step.hashes[0]



