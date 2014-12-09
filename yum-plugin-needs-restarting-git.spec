%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pluginhome /usr/lib/yum-plugins
%global commit master
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           yum-plugin-needs-restarting
Version:        1.0
Release:        1%{?dist}
Summary:        YUM plugin for listing processes using old files after upgrade
Group:          System Environment/Base
License:        GPLv2
URL:            https://github.com/stdevel/yum-plugin-needs-restarting
Source0:        https://github.com/stdevel/yum-plugin-needs-restarting/archive/%{commit}/yum-plugin-needs-restarting-%{commit}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
Requires:       python
Requires:       yum-utils

%description
yum-plugin-needs-restarting is a YUM plugin for listing processes using
old files after upgrading your system. It is based on the code of
needs-restarting which is part of the yum-utils package.

%prep
%setup -qn %{name}-%{commit}

%build
# This is a python script

%install
install -Dm 644 needs-restarting.conf %{buildroot}/%{_sysconfdir}/yum/pluginconf.d/needs-restarting.conf
install -Dm 755 needs-restarting.py %{buildroot}/%pluginhome/needs-restarting.py
%{__python} -c "import compileall; compileall.compile_dir('%{buildroot}/%pluginhome', 1)"

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING README.md
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/needs-restarting.conf
%{pluginhome}/needs-restarting.py
%{pluginhome}/needs-restarting.pyo
%{pluginhome}/needs-restarting.pyc


%changelog
* Wed Dec  3 2014 Michael Spahn <any0n3@fedoraproject.org>
- Initial spec file
