# DepHell Licenses

...


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
