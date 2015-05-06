Feature: Receive measures from sensor
  In simplest scenario, sending with GET will only collect one measure

  @1
  Scenario Outline: Device sends a new measure
    Given api_key for service "<SERVICE>"
    And the service "<SERVICE>" has been created
    And a device with device_id "<ID>"
    And the device with device_id "<ID>" has been created
    And data "<DATA>"
    When a measure is received
    Then the IoT GET response should be 200
    And context broker is notified
    And the response sent to Context Broker should include name "<IOT_RESP_NAME>" and value "<IOT_RESP_VAL>"
      | name | value |
      | t    | 15    |
      | h    | 771   |

  Examples:
    | ID         | SERVICE  | DATA     |
    | device_id1 | apikey3  | t_17     |


  @2
  Scenario Outline: Device sends several measures
    Given api_key for service "<SERVICE>"
    And the service "<SERVICE>" has been created
    And a device with device_id "<ID>"
    And the device with device_id "<ID>" has been created
    And several measures in data "<DATA>"
    When a measure is received
    Then the IoT POST response should be 200
    And context broker is notified
    And the response sent to Context Broker should include name "<IOT_RESP_NAME>" and value "<IOT_RESP_VAL>"

  Examples:
    | ID         | DATA                           | SERVICE |
    | device_id1 | temperature_17#humidity_711    | apikey3 |




  @3
  Scenario Outline: Device send a new measure
    Given a test


  Examples:
    | ID       | DATA  | SERVICE  |
    | DEVICE_1 | t_15  | service1 |



	
	
	
	
 