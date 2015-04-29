from lettuce import *

@step('Given a device with device_id (\w+)')
def check_dev_id(step, flow_id):
    world.flow_id = flow_id

@step('And data (\w+)')
def check_data(step, flow_data):
    world.flow_data = flow_data.replace('_', '|')

@step('And api_key for service (\w+)')
def check_apikey(step, flow_apikey):
    world.flow_apikey = flow_apikey

@step('When a request is sent')
def sending_req(step):
    assert True

@step('Then the IoT response should be ')
def iot_resp(step):
    assert True

@step('And the IoT body response should include id (\w+) and type (\w+) ')
def body_shape1(step, iot_id, iot_type):
    assert world.flow_id == iot_id
    print(world.flow_id)
    print(iot_id)

@step('And the IoT body response for the attributes should include name (\w+) and value (\w+)')
def body_shape2(step, iot_name, iot_val):
    name, val = world.flow_data.replace('|', ' ').split()
    assert name == iot_name
