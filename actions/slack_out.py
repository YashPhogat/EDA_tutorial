from st2common.runners.base_action import Action
import requests

class message_out(Action):
	def run (self, message):
		body = { "text": message}
<<<<<<< HEAD
		webhook_url = "https://hooks.slack.com/services/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"
=======
		webhook_url = "<slack_incoming_webhook_url>"
>>>>>>> d28b61f0e65e9f09d3c73bdf35836b86add1fabe
		response = requests.post(url=webhook_url, json=body)
		response.raise_for_status()
		
		return  {"status_code": response.status_code}
		pass
