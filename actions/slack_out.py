from st2common.runners.base_action import Action
import requests

class message_out(Action):
	def run (self, message):
		body = { "text": message}

		webhook_url = "<slack_incoming_webhook_url>"
		response = requests.post(url=webhook_url, json=body)
		response.raise_for_status()
		
		return  {"status_code": response.status_code}
		pass
