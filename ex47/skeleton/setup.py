try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Alexander Archer',
    'url': 'github.com/acarcher/lpthw',
    'author_email': 'alex@acarcher.dev',
    'version': '0.1',
    'install_requires': ['nose2'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'lpthw'
}

setup(**config)
