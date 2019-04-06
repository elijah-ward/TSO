"""
TSO Setup.py

As part of being packaged into a CLI tool,
the TSO project is configured here using setuptools

These are some commands to run against this project
    - Install and Run:    pip install -e .
    - Run Tests:          python setup.py pytest

"""


from setuptools import setup

setup(
    name='tso',
    version='0.1.0',
    description='A scheduling software used for telescope imaging applications',
    url="https://github.com/elijah-ward/TSO",
    package_dir={'': 'src'},
    packages=['tso'],

    setup_requires=[
        "pytest-runner"
    ],

    install_requires=[
        'astropy',
        'astroplan',
        'pytest',
        'pandas',
        'deap',
        'mysql-connector-python'
    ],
    entry_points={
        'console_scripts': [
            'tsocli = tso.tsocli.__main__:main'
        ]
    },

    tests_require=[
        'pytest'
    ],
    test_suite='tso'
)
