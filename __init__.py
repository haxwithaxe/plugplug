
import imp
from _config import config

__all__ = ['plugin', 'load', ]


def load(name):
	path = os.path.join(_config.get('plugin_dir'), '%s.py' % name)
	if os.path.exists(path):
		mod = load_source(name, path)
		return mod
	return None

