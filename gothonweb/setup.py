try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'gothon web app',
    'author': 'Alexander Archer',
    'url': 'github.com/acarcher/lpthw',
    'download_url': 'Where to download it.',
    'author_email': 'alex@acarcher.dev',
    'version': '0.1',
    'install_requires': ['nose2'],
    'packages': ['gothonweb'],
    'scripts': [],
    'name': 'gothonweb'
}

setup(**config)
