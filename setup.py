from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='headline',
    version='0.1',
    author='Daniel Ceglinski',
    author_email='danielceglinski@web.de',
    packages=find_packages(exclude=['docs']),
    url='https://github.com/MadaoG/headline',
    license='MIT',
    description='Produces nice headlines',
    long_description=long_description,
    install_requires=[
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
