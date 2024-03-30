from social_network_app.consts import STATUS_CODE, MESSAGE, SUCCESS_CODE, FAILURE_CODE
from social_network_app.utils import RATE_LIMITER_FRIEND_REQ

success = {STATUS_CODE: SUCCESS_CODE, MESSAGE: "Success"}
generic_error_1 = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Invalid request details"}
generic_error_2 = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Please try again after sometime"}
generic_error_3 = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Invalid response"}
invalid_credential = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Invalid Credentials"}

password_does_not_match = {STATUS_CODE: FAILURE_CODE, MESSAGE: "Password does not match"}
rate_limit_for_user = {STATUS_CODE: FAILURE_CODE, MESSAGE: f"Rate limit exceeded. You can send up to {RATE_LIMITER_FRIEND_REQ} friend requests per minute."}
invalid_user_action = {STATUS_CODE: FAILURE_CODE, MESSAGE: "You do not have permission to update this friend request."}
