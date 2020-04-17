# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="python_selenium_test",
    install_requires=[],
    extras_require={
        "dotenv": ["python-dotenv"],
        "dev": [
            "pytest",
            "tox"
        ],
    },
)
