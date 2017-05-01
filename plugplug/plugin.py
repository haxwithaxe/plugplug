
import os

from plugplug.config import Config


class Plugin:

	def __init__(self, name, service, config=None):
		self.name = name
		self.service = service
		self.config = config

	def __call__(self, *args, **kwargs):
		"""Universal entry point for services."""
		raise NotImplementedError()


config = Config()  # pylint: disable=invalid-name
