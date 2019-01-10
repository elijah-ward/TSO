from setuptools import setup

setup(
    name='tso',
    version='0.1.0',
    description='A useful module',
    url="https://github.com/elijah-ward/TSO",
    package_dir={'': 'src'},
    packages=['tso'],
    install_requires=[
        'astropy',
        'pytest',
        'deap'
    ],
    entry_points={
        'console_scripts': [
            'tsocli = src.tsocli.__main__:main'
        ]
    }
)
