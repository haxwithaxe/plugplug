
import os

from plugplug import Config


class Plugin:

	def __init__(self, name, service, config=None):
		self.name = name
		self.service = service
		self.config = config
		config_filename = os.path.join(os.path.dirname(__file__), '{}.conf'.format(self.name))
		if os.path.exists(config_filename):
			self.config = Config(config_filename)

	def __call__(self, *args, **kwargs):
		"""Universal entry point for services."""
		raise NotImplementedError()


config = Config()  # pylint: disable=invalid-name
