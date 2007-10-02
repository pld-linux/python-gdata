%define		module	gdata
#
Summary:	Google Data API for Python
Name:		python-%{module}
Version:	1.0.8
Release:	1
License:	Apache Group License v2.0
Group:		Development/Languages/Python
Source0:	http://gdata-python-client.googlecode.com/files/%{module}.py-%{version}.tar.gz
# Source0-md5:	b6f6aa192446047d8045d3c30345f1ef
URL:		http://code.google.com/p/gdata-python-client/
BuildRequires:	python >= 2.5
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Google data Python Client Library provides a library and source
code that make it easy to access data through Google Data APIs.

%prep
%setup -q -n %{module}.py-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module} -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt RELEASE_NOTES.txt
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/atom
