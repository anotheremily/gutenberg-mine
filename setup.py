try 
	from setuptools import setup
except ImportError: 
	from distutils.core import setup

config = {
	'description': 'Gutenberg Mine',
	'author': 'Zach Young',
	'url': 'http://zachyoung.org',
	'download_url': 'http://zachyoung.org',
	'author_email': 'me[at]zachyoung[dot]org',
	'version': '0.1',
	'install_requires': ['nose','redis_wrap','redis_graph','web.py'],
	'packages': ['gbmine', 'gbweb'],
	'scripts': [],
	'name': 'gbmine'
}

setup(**config)
