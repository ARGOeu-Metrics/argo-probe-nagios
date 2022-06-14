Name:		argo-probe-nagios
Version:	0.2.0
Release:	1%{?dist}
Summary:	ARGO probes for checking Nagios
License:	GPLv3+

Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}
Requires:       perl-JSON, perl-libwww-perl, perl-Nagios-Plugin, perl-GridMon
AutoReqProv: no

%description
ARGO probes for Nagios:
- probe check_nagios that remotely checks that Nagios is running
- probe gather_healthy_nodes which generates list of hostnames with a given service in status OK

%prep
%setup -q

%define _unpackaged_files_terminate_build 0

%install

install -d %{buildroot}/%{_libexecdir}/argo/probes/nagios
install -m 755 check_nagios %{buildroot}/%{_libexecdir}/argo/probes/nagios/check_nagios
install -m 755 gather_healthy_nodes %{buildroot}/%{_libexecdir}/argo/probes/nagios/gather_healthy_nodes

%files
%dir /%{_libexecdir}/argo
%dir /%{_libexecdir}/argo/probes/
%dir /%{_libexecdir}/argo/probes/nagios

%attr(0755,root,root) /%{_libexecdir}/argo/probes/nagios/check_nagios
%attr(0755,root,root) /%{_libexecdir}/argo/probes/nagios/gather_healthy_nodes

%changelog
* Tue Jun 14 2022 Katarina Zailac <katarina.zailac@gmail.com> - 0.2.0-1%{?dist}
- Add gather_healthy_nodes probe
* Thu Jun 9 2022 Katarina Zailac <katarina.zailac@gmail.com> - 0.1.0-1%{?dist}
- Add check_nagios probe
