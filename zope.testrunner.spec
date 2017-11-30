#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF2A968348913D1D8 (tseaver@palladion.com)
#
Name     : zope.testrunner
Version  : 4.7.0
Release  : 6
URL      : https://pypi.debian.net/zope.testrunner/zope.testrunner-4.7.0.zip
Source0  : https://pypi.debian.net/zope.testrunner/zope.testrunner-4.7.0.zip
Source99 : https://pypi.debian.net/zope.testrunner/zope.testrunner-4.7.0.zip.asc
Summary  : Zope testrunner script.
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.testrunner-bin
Requires: zope.testrunner-legacypython
Requires: zope.testrunner-python3
Requires: zope.testrunner-python
Requires: setuptools
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
zope.testrunner
        ***************
        
        |buildstatus|_
        |winbotstatus|_

%package bin
Summary: bin components for the zope.testrunner package.
Group: Binaries

%description bin
bin components for the zope.testrunner package.


%package legacypython
Summary: legacypython components for the zope.testrunner package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the zope.testrunner package.


%package python
Summary: python components for the zope.testrunner package.
Group: Default
Requires: zope.testrunner-legacypython
Requires: zope.testrunner-python3

%description python
python components for the zope.testrunner package.


%package python3
Summary: python3 components for the zope.testrunner package.
Group: Default
Requires: python3-core

%description python3
python3 components for the zope.testrunner package.


%prep
%setup -q -n zope.testrunner-4.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512067898
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1512067898
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/zope-testrunner

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
