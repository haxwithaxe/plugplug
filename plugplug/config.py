
import imp
import os


class ConfigException(Exception):

	def __init__(self, name, *parts, **named_parts):
		if len(parts) > 0:
			parts = list(parts)
			fmt = parts.pop(0)
			message = fmt.format(name, *parts, **named_parts)
		else:
			message = 'Error handling the configs for {}'.format(name)
		super().__init__(message)


class Config:

	def __init__(self, filename=None, values=None):
		self._filename = filename
		self.load(self._filename)
		self.update(values or {})

	def load(self, filename):
		if filename:
			self._filename = filename
			conf_mod = imp.load_source('config', self._filename)
			self.update(conf_mod.__dict__)

	def update(self, values):
		for key in tuple(values):
			if key in ('get', 'load', 'for_plugin', 'update', '_filename'):
				values.pop(key)
			if key.startswith('__'):
				values.pop(key)
		self.__dict__.update(values)

	def get(self, name, default=None, throw=False):
		if name in self:
			return self.__dict__.get(name)
		elif throw:
			raise ConfigException(name, 'No config named "{}".')
		return default

	def __contains__(self, key):
		return key in self.__dict__

	def for_plugin(self, name):
		config_filename = os.path.join(
				self.get('plugin_directory'),
				'{}.conf'.format(name)
				)
		if os.path.exists(config_filename):
			return Config(config_filename)
		if 'plugin_'+name in self:
			return Config(values=self.get('plugin_'+name))
		raise ConfigException(name, 'No plugin config for "{}".')
