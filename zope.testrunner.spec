#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zope.testrunner
Version  : 5.3.0
Release  : 52
URL      : https://files.pythonhosted.org/packages/5b/20/dd4713d6467112ed3efb8dd7b106d54818ae10a30c2ba0364e67e13f7d0b/zope.testrunner-5.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5b/20/dd4713d6467112ed3efb8dd7b106d54818ae10a30c2ba0364e67e13f7d0b/zope.testrunner-5.3.0.tar.gz
Summary  : Zope testrunner script.
Group    : Development/Tools
License  : ZPL-2.1
Requires: zope.testrunner-bin = %{version}-%{release}
Requires: zope.testrunner-license = %{version}-%{release}
Requires: zope.testrunner-python = %{version}-%{release}
Requires: zope.testrunner-python3 = %{version}-%{release}
Requires: setuptools
Requires: six
Requires: zope.exceptions
Requires: zope.interface
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.exceptions
BuildRequires : zope.interface

%description
zope.testrunner
        =================

%package bin
Summary: bin components for the zope.testrunner package.
Group: Binaries
Requires: zope.testrunner-license = %{version}-%{release}

%description bin
bin components for the zope.testrunner package.


%package license
Summary: license components for the zope.testrunner package.
Group: Default

%description license
license components for the zope.testrunner package.


%package python
Summary: python components for the zope.testrunner package.
Group: Default
Requires: zope.testrunner-python3 = %{version}-%{release}

%description python
python components for the zope.testrunner package.


%package python3
Summary: python3 components for the zope.testrunner package.
Group: Default
Requires: python3-core
Provides: pypi(zope.testrunner)
Requires: pypi(setuptools)
Requires: pypi(six)
Requires: pypi(zope.exceptions)
Requires: pypi(zope.interface)

%description python3
python3 components for the zope.testrunner package.


%prep
%setup -q -n zope.testrunner-5.3.0
cd %{_builddir}/zope.testrunner-5.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615994837
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zope.testrunner
cp %{_builddir}/zope.testrunner-5.3.0/LICENSE.md %{buildroot}/usr/share/package-licenses/zope.testrunner/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/zope-testrunner

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zope.testrunner/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
