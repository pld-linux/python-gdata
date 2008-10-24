%define		module	gdata
Summary:	Google Data API for Python
Summary(pl.UTF-8):	API Google Data dla Pythona
Name:		python-%{module}
Version:	1.2.2
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Python
Source0:	http://gdata-python-client.googlecode.com/files/%{module}.py-%{version}.tar.gz
# Source0-md5:	b4d152f04815abcbe25d901d8b4a6715
URL:		http://code.google.com/p/gdata-python-client/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Google Data Python Client Library provides a library and source
code that make it easy to access data through Google Data APIs.

%description -l pl.UTF-8
Projekt Google Data Python Client Library udostępnia wraz z kodem
bibliotekę ułatwiającą dostęp do danych poprzez API Google Data.

%prep
%setup -q -n %{module}.py-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

cp -r samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt RELEASE_NOTES.txt
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/atom
%{py_sitescriptdir}/gdata.py-*.egg-info
%{_examplesdir}/%{name}-%{version}
