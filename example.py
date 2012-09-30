
import plugin

class Plugin(plugin.Plugin):
	def __init__(self):
		self.output = ''

	def inputs(self, *args, **kwargs):
		'''input from main system is given here
			return None
		'''
		self.output = args[0]

	def outputs(self, *args, **kwargs):
		'''output from plugin is returned here
			return output or None if no output
		'''
		if 'caps' in args or ('caps' in kwargs and kwargs['caps']):
			return self.output.upper()
		return self.output

	def errors(self, *args, **kwargs):
		'''return error messages or secondary output here
			return Exceptions, strings, or None if no error output
		'''
		return None

if __name__ == '__main__':
	plug = Plugin()
	plug.inputs('hello world')
	print(plug.outputs())
	print(plug.outputs('caps'))
	print(plug.outputs(caps=True))
	plug.errors()

