#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vuln-chain-joshbressers", # Replace with your own username
    version="0.0.1",
    author="Josh Bressers",
    author_email="josh@bress.net",
    description="A library for storing vulnerability info in a blockchain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshbressers/dwf-chain",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
