# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os

from setuptools import setup, find_packages

dir_path = os.path.dirname(os.path.realpath(__file__))

def read_requirements_file(filename):
    req_file_path = "%s/%s" % (dir_path, filename)
    with open(req_file_path) as f:
        return [line.strip() for line in f]

setup(
    name="pyrbgt",
    version="0.0.1",
    author="PyRobot Team",
    url="https://github.com/facebookresearch/pyrobot.git",
    license="MIT",
    python_requires='>=3.6',
    package_dir={"": "src"},
    packages=["pyrbgt"],
    install_requires=read_requirements_file("requirements.txt"),
)