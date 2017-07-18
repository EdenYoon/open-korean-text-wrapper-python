# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Jaepil Jeong, Originated by
# Copyright (c) 2017 Eden Yoon, Modified by

from __future__ import print_function

import os

from setuptools import setup
from setuptools.command.install import install

try:
    from urllib import urlretrieve
except:
    from urllib.request import urlretrieve


__VERSION__ = "0.2.4"

_JAVA_LIB_URLS = [
    "http://central.maven.org/maven2/org/scala-lang/scala-library/2.12.2/scala-library-2.12.2.jar",
    "https://repo1.maven.org/maven2/com/twitter/twitter-text/1.14.7/twitter-text-1.14.7.jar",
    "https://repo1.maven.org/maven2/org/openkoreantext/open-korean-text/2.1.0/open-korean-text-2.1.0.jar"
]
_PATH_TO_LIB = os.path.join(os.path.abspath(os.path.dirname((__file__))), "openkoreantext/data/lib")


class InstallCommand(install):
    @staticmethod
    def download_jars(target_path):
        for url in _JAVA_LIB_URLS:
            jar_name = os.path.basename(url)
            jar_path = os.path.join(target_path, jar_name)
            if not os.path.exists(jar_path):
                print("Downloading java package:", jar_name)
                print("Saved java package to:", jar_path)
                urlretrieve(url, jar_path)

    def run(self):
        self.download_jars(target_path=_PATH_TO_LIB)
        install.run(self)


setup(
    name="OpenKoreanText",
    license="Apache 2.0",
    version=__VERSION__,
    packages=["openkoreantext"],
    package_dir={"openkoreantext": "openkoreantext"},
    package_data={
        "openkoreantext": [
            "data/lib/*.jar",
        ],
    },
    install_requires=[
        "JPype1"
    ],
    author="Eden Yoon",
    author_email="yolha79@gmail.com",
    url="https://github.com/EdenYoon/open-korean-text-wrapper-python",
    download_url="https://github.com/EdenYoon/open-korean-text-wrapper-python/tree/master",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: Korean",
        "Programming Language :: Java",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic"
    ],
    platforms=[
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    keywords=[
        "open-korean-text",
        "openkoreantext",
        "morphological analyzer",
        "morphology", "analyzer",
        "korean", "tokenizer"
    ],
    description="Python interface to open-korean-text, a Korean morphological analyzer.",
    cmdclass={
        'install': InstallCommand,
    }
)
