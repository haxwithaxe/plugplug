
import abc

class Plugin(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def inputs(self, *args, **kwargs):
		'''input from main system is given here
			return None
		'''
		pass

	@abc.abstractmethod
	def outputs(self, *args, **kwargs):
		'''output from plugin is returned here
			return output or None if no output
		'''
		return

	@abc.abstractmethod
	def errors(self, *args, **kwargs):
		'''return error messages or secondary output here
			return Exceptions, strings, or None if no error output
		'''
		return
