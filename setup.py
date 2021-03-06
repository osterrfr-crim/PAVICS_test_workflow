#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pavics_wps_test_run.__meta__ import __version__, __author__, __email__

with open('README.rst') as readme_file:
    README = readme_file.read()

with open('HISTORY.rst') as history_file:
    HISTORY = history_file.read().replace('.. :changelog:', '')

REQUIREMENTS = [
    "owslib",
    "lxml"
]

TEST_REQUIREMENTS = [
    'nose',
    # TODO: put package test requirements here
]

setup(
    # -- meta information --------------------------------------------------
    name='pavics_wps_test_run',
    version=__version__,
    description="This project acts as a WPS client to run a workflow through WPS.",
    long_description=README + '\n\n' + HISTORY,
    author=__author__,
    author_email=__email__,
    url='https://github.com/osterrfr-crim/pavics_wps_test_run',
    platforms=['linux_x86_64'],
    license="ISCL",
    keywords='pavics_wps_test_run',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # -- Package structure -------------------------------------------------
    packages=[
        'pavics_wps_test_run',
    ],
    package_dir={'pavics_wps_test_run':
                 'pavics_wps_test_run'},
    include_package_data=True,
    install_requires=REQUIREMENTS,
    zip_safe=False,

    # -- self - tests --------------------------------------------------------
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,

    # -- script entry points -----------------------------------------------
    entry_points={'console_scripts':
        ["run_workflow=pavics_wps_test_run.pavics_wps_test_run:main"]}
)
