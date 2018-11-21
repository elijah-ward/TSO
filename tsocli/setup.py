from setuptools import setup

setup(
    name='tsocli',
    version='0.1.0',
    packages=['tsocli'],
    entry_points={
        'console_scripts': [
            'tsocli = tsocli.__main__:main'
        ]
    })
