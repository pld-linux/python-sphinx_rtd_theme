#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module
%bcond_without	tests	# unit tests

%define 	module	sphinx_rtd_theme
Summary:	ReadTheDocs.org theme for Sphinx
Summary(pl.UTF-8):	Motyw ReadTheDocs.org dla Sphinksa
Name:		python-%{module}
Version:	1.0.0
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx_rtd_theme/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_rtd_theme/%{module}-%{version}.tar.gz
# Source0-md5:	fdfc7d2e102cb96eca0f6155dde7403e
Patch0:		%{name}-docutils.patch
URL:		https://github.com/snide/sphinx_rtd_theme/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
BuildRequires:	python-readthedocs-sphinx-ext
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-readthedocs-sphinx-ext
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a mobile-friendly Sphinx theme made for readthedocs.org.

%description -l pl.UTF-8
Ten pakiet zawiera przyjazny dla urządzeń przenośnych motyw Sphinksa
wykonany przez readthedocs.org.

%package -n python3-%{module}
Summary:	ReadTheDocs.org theme for Sphinx
Summary(pl.UTF-8):	Motyw ReadTheDocs.org dla Sphinksa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
This is a mobile-friendly Sphinx theme made for readthedocs.org.

%description -n python3-%{module} -l pl.UTF-8
Ten pakiet zawiera przyjazny dla urządzeń przenośnych motyw Sphinksa
wykonany przez readthedocs.org.

%prep
%setup -q -n %{module}-%{version}
%patch -P0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
