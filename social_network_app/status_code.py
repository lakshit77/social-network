from social_network_app.consts import STATUS_CODE, MESSAGE, SUCCESS_CODE, FAILURE_CODE

success = {STATUS_CODE: SUCCESS_CODE, MESSAGE: "Success"}
generic_error_1 = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Invalid request details"}
generic_error_2 = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Please try again after sometime"}

password_does_not_match = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Password does not match"}
