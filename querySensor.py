import json
import subprocess
import paho.mqtt.client as mqtt
import numpy
from threading import Event, Thread

def call_repeatedly(interval, func, *args):
	stopped = Event()
	def loop():
		while not stopped.wait(interval):
			func(*args)
	Thread(target=loop).start()
	return stopped.set

def queryRehau():
	d={"voc":0}
	p=subprocess.Popen(['sudo', '/home/pi/airsensor', '-o', '-v'], stdout=subprocess.PIPE, shell=False, universal_newlines=True)
        #p=subprocess.Popen(["/home/pi/sudo ./airsensor -o -v"], stdout=subprocess.PIPE, shell=False, universal_newlines=True)

	(output, err) = p.communicate()
	p.wait()

	if "Error:" not in output:
		newVal=output
		#newVal=numpy.random.randint(10,40)
		#values should be between 450 and 2000
		d["voc"] = newVal
		print(json.dumps(d))

		try:
			client = mqtt.Client("rehau")
			#client.username_pw_set(secrect_dict['mqtt_user'], secret_dict['mqtt_pass'])
			client.connect("localhost")
			client.publish("rehau", json.dumps(d))
			client.disconnect()
		except (RuntimeError,ValueError,IOError):
			print("could not connect to homeassist")



import logging
import logging.handlers

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')

my_logger.addHandler(handler)

my_logger.debug('this is debug')
my_logger.critical('this is critical')

cancel_future_calls = call_repeatedly(60, queryRehau)
#cancel_future_calls()
