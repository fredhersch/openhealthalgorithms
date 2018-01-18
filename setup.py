import subprocess
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()


def find_packages(*args, **kwargs):
    return ['OHA', 'OHA.param_builders', 'OHA.assessments', 'tests']


def version():
    __version = '0.2.3'
    __tag = 'b'
    if path.exists('.git'):
        __tag = 'git'
        __build = subprocess.check_output('git rev-list HEAD --count'.split()).decode().strip()
    else:
        __build = __tag
    return '%s.%s.%s' % (__version, __tag, __build)


setup(
    version=version(),
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    include_package_data=True,
)
