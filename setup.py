from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-secret-key',
    version='1.0.1',
    scripts=['django-secret-key'],
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Generate SECRET KEY',
    long_description='Generate random Django SECRET KEY',
    install_requires=['django'],
    url='http://github.com/ariestiyansyah/django-secret-key',
    author='Rizky Ariestiyansyah',
    author_email='ariestiyansyah.rizky@gmail.com'
)
