Feature: Receive measures from sensor
  In simplest scenario, sending with GET will only collect one measure

  Scenario Outline: Send data with GET to new device
    Given a device with device_id "<ID>"
    And data "<DATA>"
    And api_key for service "<SERVICE>"
    When a request is sent
    Then the IoT response should be 200
    And the IoT body response should include id "<IOT_RESP_ID>" and type "<IOT_RESP_TYPE>"
      | id        | type  |
      | thing:001 | thing |
    And the IoT body response for the attributes should include name "<IOT_RESP_NAME>" and value "<IOT_RESP_VAL>"
      | name | value |
      | t    | 15    |


  Examples:
    | ID    | DATA  | SERVICE  | IOT_RESP_ID | IOT_RESP_TYPE | IOT_RESP_NAME | IOT_RESP_VAL | STATUS
    | FLOW0 | t_15  | service1 | FLOW0       | temperature   | t             | 15           | UPDATED
    | FLOW1 | h_771 | service1 | FLOW1       | humidity      | h             | 771          | UPDATED

 # Using | to separate data is not possible --> _ instead
	


	
	
