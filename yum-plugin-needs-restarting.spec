%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pluginhome /usr/lib/yum-plugins

Name:           yum-plugin-needs-restarting
Version:        1.0
Release:        1%{?dist}
Summary:        YUM plugin for listing processes using old files after upgrade
Group:          System Environment/Base
License:        GPLv2
URL:            https://github.com/stdevel/yum-plugin-needs-restarting
Source0:        https://github.com/stdevel/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
Requires:       python
Requires:       yum-utils

%description
yum-plugin-needs-restarting is a YUM plugin for listing processes using
old files after upgrading your system. It is based on the code of
needs-restarting which is part of the yum-utils package.

%prep
%setup -q -n %{name}-%{version}
cp -a LICENSE COPYING

%build
# This is a python script

%install
install -Dm 644 needs-restarting.conf %{buildroot}/%{_sysconfdir}/yum/pluginconf.d/needs-restarting.conf
install -Dm 755 needs-restarting.py %{buildroot}/%pluginhome/needs-restarting.py

%clean
rm -rf %{buildroot}

%files
%license COPYING
%doc README.md
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/needs-restarting.conf
%{pluginhome}/needs-restarting.py*

%changelog
* Tue Jan 27 2015 - Michael Spahn <any0n3@fedoraproject.org>
- Fix serveral issues

* Wed Dec 3 2014 - Michael Spahn <any0n3@fedoraproject.org>
- Initial spec file
