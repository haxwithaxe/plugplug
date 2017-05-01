
from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'plugplug/__init__.py')) as fp:
    exec(fp.read())

setup(
    name='plugplug',
    version=__version__,
    description='A plugin framwork.',
    long_description=__doc__,
    url='https://github.com/haxwithaxe/plugplug',
    author=__author__,
    author_email=__contact__,
    license=__license__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
    ],
    keywords='plugplug setuptools development plugin',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'example']),
)
