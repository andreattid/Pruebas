Feature: Testing UL2.0 features within ORION CONTEXT BROKER
  Sending measures from sensor with UL2.0 protocol, through an IOT Agent, with REST operations.
  Collecting those measures in Context Broker and retrieving them.
  Also, sending information from Context Broker to the sensor using the same path but backwards, as commands.

  @1
  Scenario Outline: Device sends a new measure
    Given api_key for service "<SERVICE>" and device_id "<ID>" and data "<DATA>"
    And the service has been created
    When a measure is sent to IoT Agent using GET
    Then the IoT GET response should be 200
    And context broker is notified
    And the response sent to Context Broker should include
      | name | value |
      | t    | 15    |
      | h    | 771   |

  Examples:
    | ID   | SERVICE | DATA |
    | dev1 | abcabc  | r_6  |


  @2
  Scenario Outline: Device sends several measures
    Given api_key for service "<SERVICE>" and device_id "<ID>" and data
      | data        | value |
      | temperature | 17    |
      | humidity    | 711   |
    And the service has been created
    When a measure is sent to IoT Agent using POST
    Then the IoT POST response should be 200
    And context broker is notified
    And the response sent to Context Broker should include

  Examples:
    | ID         | SERVICE |
    | device_id1 | abcabc  |


  # Scenario Outline: Device receives command from CB


  @4
  Scenario Outline: Device send a new measure
    Given a test

  Examples:
    | ID       | DATA | SERVICE  |
    | DEVICE_1 | t_15 | service1 |