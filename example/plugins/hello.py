
from plugplug.plugin import Plugin


class MyPlugin(Plugin):

	def __call__(self, name=None):
		if name:
			self.service.send(self, 'hello {}'.format(name))
			return 'hello {}'.format(name)
		else:
			self.service.error(self, 'No name given.')

	def test(self):
		print(self.config.__dict__)

def load(service, config):
	return MyPlugin(__name__, service, config)
