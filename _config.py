default_config_file = 'pluginplugin.conf'

class Config(object):
	def __init__(self, config_file=None):
		self.config_file = config_file
		self.config_vals = {}
	def get(self, *args):
		if len(args) == 1:
			if args[0] in self.config_vals:
				return self.config_vals[args[0]]
			return None
		else:
			return_dict = {}
			for a in args:
				if a in self.config_vals:
					return_dict[a] = self.config_vals[a]
				else:
					return_dict[a] = None
			return return_dict

	def set(self, **kwargs):
		for key, val in kwargs:
			self.config_vals[key] = val
		return True

config = Config(default_config_file)
