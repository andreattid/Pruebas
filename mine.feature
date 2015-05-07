Feature: Testing UL2.0 features within ORION CONTEXT BROKER
  Sending measures from sensor with UL2.0 protocol, through an IOT Agent, with REST operations.
  Collecting those measures in Context Broker and retrieving them.
  Also, sending information from Context Broker to the sensor using the same path but backwards, as commands.

  @1
  Scenario Outline: Device sends a new measure
    Given api_key for service "<SERVICE>" and device_id "<ID>"  and data "<DATA>"
    And the service has been created
    And the device has been created
    When a measure is sent to IoT Agent with a certain IP
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


  # Scenario Outline: Device receives command from CB


  @4
  Scenario Outline: Device send a new measure
    Given a test

  Examples:
    | ID       | DATA  | SERVICE  |
    | DEVICE_1 | t_15  | service1 |



	
	
	
	
 