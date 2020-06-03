import requests
import reverse_geocode
import json

from st2reactor.sensor.base import PollingSensor

class ISS_Sensor(PollingSensor):

    def setup(self) :
        # Setup stuff goes here. For example, you might establish connections
        # to external system once and reuse it. This is called only once by the system.
        self.logger = self.sensor_service.get_logger(name= self.__class__.__name__)
        pass

    def poll(self) :
        # This is where the crux of the sensor work goes.
        # This is called once by the system.
        # (If you want to sleep for regular intervals and keep
        # interacting with your external system, you'd inherit from PollingSensor.)
        # For example, let's consider a simple flask app. You'd run the flask app here.
        # You can dispatch triggers using sensor_service like so:
        # self.sensor_service(trigger, payload, trace_tag)
        #   # You can refer to the trigger as dict
        #   # { "name": ${trigger_name}, "pack": ${trigger_pack} }
        #   # or just simply by reference as string.
        #   # i.e. dispatch(${trigger_pack}.${trigger_name}, payload)
        #   # E.g.: dispatch('examples.foo_sensor', {'k1': 'stuff', 'k2': 'foo'})
        #   # trace_tag is a tag you would like to associate with the dispatched TriggerInstance
        #   # Typically the trace_tag is unique and a reference to an external event.

        poll_response = requests.get(url="http://api.open-notify.org/iss-now.json")
        iss_dict = poll_response.json()
        coordinate = (iss_dict['iss_position']['latitude'], iss_dict['iss_position']['longitude'])

        location = reverse_geocode.search([coordinate])[0]
        iss_country = location['country']

        previous_country = self.sensor_service.get_value(name = 'last_iss_loc', local = False)
	if previous_country == iss_country:
		return
	self.sensor_service.set_value(name = 'last_iss_loc', value = iss_country, local= False)
	if iss_country == "India":
		self.sensor_service.dispatch(
            	trigger = "eda_tutorial.ISS_Detail",
            	payload = {
                	"country": iss_country
            		}
        	)

        pass

    def cleanup(self) :
        # This is called when the st2 system goes down. You can perform cleanup operations like
        # closing the connections to external system here.
        pass

    def add_trigger(self, trigger) :
        # This method is called when trigger is created
        pass

    def update_trigger(self, trigger) :
        # This method is called when trigger is updated
        pass

    def remove_trigger(self, trigger) :
        # This method is called when trigger is deleted
        pass

