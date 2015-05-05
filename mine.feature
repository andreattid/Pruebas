Feature: Receive measures from sensor
	In simplest scenario, sending with GET will only collect one measure

Scenario Outline: Device send a new measure
	Given api_key for service "<SERVICE>"
    And the service "<SERVICE>" has been created
    And a device with device_id "<ID>"
    And the device with device_id "<ID>" has been created
	And data "<DATA>"
	When a measure is received
	Then the IoT response should be 200
	And context broker is notified
    And the response sent to Context Broker should include name "<IOT_RESP_NAME>" and value "<IOT_RESP_VAL>" and id "<IOT_RESP_ID>"
                                |name          |value     |id            |
								|t             |15        |flow0         |
                                |h             |771       |flow1         |


Examples:
    | ID          | DATA    | SERVICE  |
    | DEVICE_1    | t_15    | service1 |
    | DEVICE_2    | h_771   | service1 |

	# Using | to separate data is not possible --> _ instead
	


	
	
	
	
 