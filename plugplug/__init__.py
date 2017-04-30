
from imp import load_source
from os.path import exists, join
import sys


class ConfigException(Exception):

	def __init__(self, name, *parts, **named_parts):
		if len(parts) > 0:
			parts = list(parts)
			fmt = parts.pop(0)
			message = fmt.format(name, *parts, **named_parts)
		else:
			message = 'Error handling the configs for {}'.format(name)
		super().__init__(message)


class Configlet:

	def __init__(self, configs):
		self.__dict__.update(configs)


class Config:

	__config = None

	def __init__(self, filename=None):
		self._filename = filename
		self.load(self._filename)

	def load(self, filename):
		if filename:
			self._filename = filename
			self.__config = load_source('config', self._filename)

	def get(self, name, default=None, throw=False):
		if name in self.__config.__dict__:
			return self.__config.__dict__[name]
		elif throw:
			raise ConfigException(name, 'No config named "{}".')
		return default

	def for_plugin(self, name):
		if 'plugin_'+name not in self.__config.__dict__:
			raise ConfigException(name, 'No plugin config for "{}".')
		return Configlet(self.__config.__dict__['plugin_'+name])

	def __getattr__(self, attr):
		if hasattr(self.__config, attr):
			return getattr(self.__config, attr)


config = Config()  # pylint: disable=invalid-name
