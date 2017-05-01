
import imp
import logging
import os

from plugplug.plugin import Plugin


class Service:

	def __init__(self, name, config):
		self.name = name
		self.config = config
		self._logger = logging.getLogger(name=self.config.get('logger_name'))
		self._debug = self._logger.debug
		self._info = self._logger.info
		self._warn = self._logger.warn
		self._error = self._logger.error

	def load_plugin(self, plugin_name):
		path = os.path.join(self.config.get('plugin_directory'), '%s.py' % plugin_name)
		if os.path.exists(path):
			mod = imp.load_source(plugin_name, path)
			self._debug('Imported plugin "%s"', plugin_name)
			return mod.load(self, self.config.for_plugin(plugin_name))
		self._error('Failed to load plugin "%s"', plugin_name)
		return None

	def send(self, source, *args, **kwargs):
		if isinstance(source, Plugin):
			source = source.name
		self._info('"%s" sent "%s"', source, *args, **kwargs)

	def error(self, source, message, *args, **kwargs):
		if isinstance(source, Plugin):
			source = source.name
		self._error('%s: "%s"', source, message, **kwargs)
