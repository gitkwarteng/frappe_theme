from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappe_theme/__init__.py
from frappe_theme import __version__ as version

setup(
	name='frappe_theme',
	version=version,
	description='Custom Frappe theme',
	author='e8 Technologies',
	author_email='e8technologies.gh@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
