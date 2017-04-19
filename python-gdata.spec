#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	gdata
Summary:	Google Data API for Python
Summary(pl.UTF-8):	API Google Data dla Pythona
Name:		python-%{module}
Version:	2.0.18
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/gdata
Source0:	https://pypi.python.org/packages/source/g/gdata/%{module}-%{version}.tar.gz
# Source0-md5:	13b6e6dd8f9e3e9a8e005e05a8329408
URL:		https://github.com/google/gdata-python-client
BuildRequires:	python >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Google Data Python Client Library provides a library and source
code that make it easy to access data through Google Data APIs.

%description -l pl.UTF-8
Projekt Google Data Python Client Library udostępnia wraz z kodem
bibliotekę ułatwiającą dostęp do danych poprzez API Google Data.

%package apidocs
Summary:	Google Data Python module documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja modułu Pythona Google Data w formacie HTML
Group:		Documentation

%description apidocs
Google Data Python module documentation in HTML format.

%description apidocs -l pl.UTF-8
Dokumentacja modułu Pythona Google Data w formacie HTML.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-2/lib %{__python} tests/run_data_tests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

cp -pr samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt RELEASE_NOTES.txt
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/atom
%{py_sitescriptdir}/gdata-*.egg-info
%{_examplesdir}/%{name}-%{version}

%files apidocs
%defattr(644,root,root,755)
%doc pydocs/*.html
