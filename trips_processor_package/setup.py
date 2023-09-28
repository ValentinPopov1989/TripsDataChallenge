'''
To install in developer mode (editable after installation):
in the parent directory 'exercise_package', run:
pip install -e ./   OR EQUIVALENTLY: python setup.py develop

'''

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='trips-processor',
    description='trips-processor',
    author='ValentinPopov',
    # Where is the source code:
    package_dir = {'' : '.'}, #this directory

    # Include all packages you find under exercise:
    packages=find_packages(where='.',include='trips_processor/*')
)
