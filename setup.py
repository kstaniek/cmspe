# =============================================================================
#
# Copyright (c) 2016, Cisco Systems
# All rights reserved.
#
# # Author: Klaudiusz Staniek
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
# =============================================================================


from setuptools import setup, find_packages
import re
from uuid import uuid4


install_requires = [
    "stevedore",
    "pkginfo",
    "click",
    "condoor",
]


def version():
    pyfile = 'csmpe/__init__.py'
    with open(pyfile) as fp:
        data = fp.read()

    match = re.search("__version__ = '([^']+)'", data)
    assert match, 'cannot find version in {}'.format(pyfile)
    return match.group(1)


setup(
    name='csmpe',
    version=version(),
    description='CSM Plugin Engine',
    author='Klaudiusz Staniek',
    author_email='klstanie@cisco.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'csmpe = csmpe.__main__:cli',
        ],
        'csm.plugin': [
            '{} = csmpe.core_plugins.csm_config_capture.asr9k:Plugin'.format(uuid4()),
            '{} = csmpe.core_plugins.csm_failed_config_startup_check.asr9k:Plugin'.format(uuid4()),
            '{} = csmpe.core_plugins.csm_custom_commands_capture.plugin:Plugin'.format(uuid4()),
            '{} = csmpe.core_plugins.csm_redundancy_check.plugin:Plugin'.format(uuid4()),
            '{} = csmpe.core_plugins.csm_node_status_check.plugin:Plugin'.format(uuid4()),
            '{} = csmpe.core_plugins.csm_filesystem_check.disk_space_check:Plugin'.format(uuid4()),
            '{} = csmpe.core_plugins.csm_filesystem_check.filesystem_rw_check:Plugin'.format(uuid4()),
            '{} = csmpe.core_plugins.csm_install_operations.add_asr9k:Plugin'.format(uuid4()),
            '{} = csmpe.core_plugins.csm_install_operations.remove_asr9k:Plugin'.format(uuid4()),
            '{} = csmpe.core_plugins.csm_install_operations.deactivate_asr9k:Plugin'.format(uuid4()),
            '{} = csmpe.core_plugins.csm_install_operations.activate_asr9k:Plugin'.format(uuid4()),
            '{} = csmpe.core_plugins.csm_check_config_filesystem.plugin:Plugin'.format(uuid4()),

        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe=False,
    install_requires=install_requires,
    tests_requires=['nose', 'flake8'],
    package_data={'': ['LICENSE', ], },
)
