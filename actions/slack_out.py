from st2common.runners.base_action import Action
import requests

class message_out(Action):
	def run (self, message):
		body = { "text": message}
		webhook_url = "https://hooks.slack.com/services/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"
		response = requests.post(url=webhook_url, json=body)
		response.raise_for_status()
		
		return  {"status_code": response.status_code}
		pass
