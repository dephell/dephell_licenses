# DepHell Licenses

[![travis](https://travis-ci.org/dephell/dephell_licenses.svg?branch=master)](https://travis-ci.org/dephell/dephell_licenses)
[![appveyor](https://ci.appveyor.com/api/projects/status/github/dephell/dephell_licenses?svg=true)](https://ci.appveyor.com/project/orsinium/dephell-licenses)
[![MIT License](https://img.shields.io/pypi/l/dephell-licenses.svg)](https://github.com/dephell/dephell_licenses/blob/master/LICENSE)

Manage OSS licenses: retrieve information, generate.

## Installation

Install from [PyPI](https://pypi.org/project/dephell-licenses/):

```bash
python3 -m pip install --user dephell_licenses
```

## Usage

```python
from dephell_licenses import licenses

# ways to get a license:
license = licenses.get_by_id('MIT')
license = licenses.get_by_name('MIT License')
license = licenses.get_by_classifier('License :: OSI Approved :: MIT License')

# license object
license
# License(id='MIT', classifier='License :: OSI Approved :: MIT License', name='MIT License', approved=True, deprecated=False, links=['https://opensource.org/licenses/MIT'], url='http://spdx.org/licenses/MIT.json')

# generate license
license.make_text(copyright='2019 Gram')
# 'MIT License\n\nCopyright (c) 2019 Gram\n\nPermission is hereby granted ...'
```

## Most popular licenses

```bash
go run stat.go | grep "License :: " | perl -F"\|" -lane 'print $F[0] if $F[1]>100' | sort
```

There is the full list of the license classifiers with more than 100 projects that uses it:

```
License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
License :: DFSG approved
License :: Free for non-commercial use
License :: Freely Distributable
License :: Freeware
License :: OSI Approved
License :: OSI Approved :: Apache Software License
License :: OSI Approved :: BSD License
License :: OSI Approved :: GNU Affero General Public License v3
License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)
License :: OSI Approved :: GNU General Public License (GPL)
License :: OSI Approved :: GNU General Public License v2 (GPLv2)
License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)
License :: OSI Approved :: GNU General Public License v3 (GPLv3)
License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)
License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)
License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
License :: OSI Approved :: ISC License (ISCL)
License :: OSI Approved :: MIT License
License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)
License :: OSI Approved :: Python Software Foundation License
License :: OSI Approved :: Zope Public License
License :: Other/Proprietary License
License :: Public Domain
License :: Repoze Public License
```
