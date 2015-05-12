Feature: Testing UL2.0 features within ORION CONTEXT BROKER
  Sending measures from sensor with UL2.0 protocol, through an IOT Agent, with REST operations.
  Collecting those measures in Context Broker and retrieving them.
  Also, sending information from Context Broker to the sensor using the same path but backwards, as commands.

  @1
  Scenario Outline: Device sends a new measure
    Given api_key for service "<SERVICE>" and device_id "<ID>" and data values
      | name | value |
      | t    | 15    |
      | h    | 771   |
    And the service has been created
    When a measure is sent to IoT Agent using GET
    Then the IoT GET response should be 200
    And context broker is notified
    And the response sent to Context Broker should match with the data sent


  Examples:
    | ID         | SERVICE  |
    | dev91      | abcabc   |


  @2
  Scenario Outline: Device sends several measures
    Given api_key for service "<SERVICE>" and device_id "<ID>" and data values
      | name           | value        |
      | abecedario     | dsa          |
      | b1             | 111          |
      | c              | dsa          |
      | d              | 111          |
      | e              | dsa          |


    And the service has been created
    When a measure is sent to IoT Agent using POST
    Then the IoT POST response should be 200
    And context broker is notified
    And the response sent to Context Broker should match with the data sent

  Examples:
    | ID          | SERVICE |
    | dev92       | abcabc  |


  # Scenario Outline: Device receives command from CB


  @4
  Scenario Outline: Device send a new measure
    Given a test

  Examples:
    | ID       | DATA  | SERVICE  |
    | DEVICE_1 | t_15  | service1 |



    """
      | f              | 111          |
      | g              | dsa          |
      | h              | 111          |
      | i              | dsa          |
      | j              | 111          |
      | k              | dsa          |
      | l              | 111          |
    """