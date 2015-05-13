Feature: Testing UL2.0 features within ORION CONTEXT BROKER
  Sending measures from sensor with UL2.0 protocol, through an IOT Agent, with REST operations.
  Collecting those measures in Context Broker and retrieving them.
  Also, sending information from Context Broker to the sensor using the same path but backwards, as commands.

  @1
  Scenario Outline: Device sends a new measure, succeed cases
    Given api_key for service "<SERVICE>" and device_id "<ID>" and data values
        | name            | value            |
        |  nam1           |  111             |
        |  1234           |  abc             |
        |  **ab           |  nnn             |
        |  xy.2           |  000             |
        |  1,23           |  111             |
        |  2_4a           |  222             |
        |  3^41           |  333             |
        |  @1520          |  444             |
        |  $$15           |  bbb             |
        |  1615a          |  nam1            |
        |  abcde          |  1234            |
        |  nnn            |  **ab            |
        |  000            |  xy.2            |
        |  111            |  1,23            |
        |  2x2            |  2_4a            |
        |  333            |  3^41            |
        |  444            |  @1520           |
        |  555            |  $$15            |
        |  666            |  %value          |
        |  %value         |  666             |
    And the service has been created
    When a measure is sent to IoT Agent using GET
    Then the IoT GET response should be 200
    And context broker is notified
    And the response sent to Context Broker should match with the data sent


  Examples:
    | ID                 | SERVICE  |
    | dev_test           | abcabc   |

 @2
  Scenario Outline: Device sends a new measure, failure cases
    Given api_key for service "<SERVICE>" and device_id "<ID>" and data values
        # No pasa estos atributos como tal, y no crea el dispositivo
        | name            | value            |
        |  &esc           |  abc             |
        |  (ds)           |  nnn             |
        |  "esto"         |  000             |
        |  abc            |  &esc            |
        |  nnn            |  (ds)            |
        |  000            |  "esto"          |


    And the service has been created
    When a measure is sent to IoT Agent using GET
    Then the IoT GET response should be 200
    And context broker is notified
    And the response sent to Context Broker should match with the data sent


  Examples:
    | ID                     | SERVICE  |
    | dev_fail               | abcabc   |



  @3
  Scenario Outline: Device sends several measures
    Given api_key for service "<SERVICE>" and device_id "<ID>" and data values
      | name                   | value        |
      | alpha                  | 125152       |
      | beta                   | rodx2        |
      | gamma                  | gg6216       |
      | phi                    | y1273        |
    And the service has been created
    When a measure is sent to IoT Agent using POST
    Then the IoT POST response should be 200
    And context broker is notified
    And the response sent to Context Broker should match with the data sent

  Examples:
    | ID          | SERVICE |
    | devdos       | abcabc  |


  # Scenario Outline: Device receives command from CB


  @4
  Scenario Outline: Device send a new measure
    Given a test

  Examples:
    | ID       | DATA  | SERVICE  |
    | DEVICE_1 | t_15  | service1 |



