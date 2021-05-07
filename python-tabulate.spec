#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-tabulate
Version  : 0.8.7
Release  : 20
URL      : https://files.pythonhosted.org/packages/57/6f/213d075ad03c84991d44e63b6516dd7d185091df5e1d02a660874f8f7e1e/tabulate-0.8.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/6f/213d075ad03c84991d44e63b6516dd7d185091df5e1d02a660874f8f7e1e/tabulate-0.8.7.tar.gz
Summary  : Pretty-print tabular data
Group    : Development/Tools
License  : MIT
Requires: python-tabulate-bin = %{version}-%{release}
Requires: python-tabulate-license = %{version}-%{release}
Requires: python-tabulate-python = %{version}-%{release}
Requires: python-tabulate-python3 = %{version}-%{release}
Requires: wcwidth
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : wcwidth

%description
===============
        
        Pretty-print tabular data in Python, a library and a command-line
        utility.

%package bin
Summary: bin components for the python-tabulate package.
Group: Binaries
Requires: python-tabulate-license = %{version}-%{release}

%description bin
bin components for the python-tabulate package.


%package license
Summary: license components for the python-tabulate package.
Group: Default

%description license
license components for the python-tabulate package.


%package python
Summary: python components for the python-tabulate package.
Group: Default
Requires: python-tabulate-python3 = %{version}-%{release}

%description python
python components for the python-tabulate package.


%package python3
Summary: python3 components for the python-tabulate package.
Group: Default
Requires: python3-core
Provides: pypi(tabulate)

%description python3
python3 components for the python-tabulate package.


%prep
%setup -q -n tabulate-0.8.7
cd %{_builddir}/tabulate-0.8.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588884461
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

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-tabulate
cp %{_builddir}/tabulate-0.8.7/LICENSE %{buildroot}/usr/share/package-licenses/python-tabulate/3b682b146c946a835c20fbc63eff54e91e3a8ef2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tabulate

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-tabulate/3b682b146c946a835c20fbc63eff54e91e3a8ef2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
