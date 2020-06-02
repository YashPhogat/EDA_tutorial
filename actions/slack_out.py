from st2common.runners.base_action import Actions
import requests

class message_out(Action):
	def run (self, message):
		body = { "text": message}
		url = 'https://hooks.slack.com/services/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'
		response = requests.post(url = url, json= body)
		response.raise_for_status()
		
		return  {"status_code": response.status_code}
		pass
