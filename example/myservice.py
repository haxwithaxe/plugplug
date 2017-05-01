
import sys

from plugplug import config
from plugplug.service import Service

class MyService(Service):

	def __init__(self, config):
		super().__init__('myservice', config)
		self.hello = self.load_plugin('hello')

	def hello_world(self):
		print(self.hello('world'))


MyService(config.Config('example/myservice.conf')).hello_world()
