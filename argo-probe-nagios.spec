Name:		argo-probe-nagios
Version:	0.1.0
Release:	1%{?dist}
Summary:	ARGO probe checking that Nagios runs
License:	GPLv3+

Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}
Requires:       perl-JSON, perl-libwww-perl, perl-Nagios-Plugin, perl-GridMon
AutoReqProv: no

%description
ARGO probe that remotely checks that Nagios is running

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_libexecdir}/argo/probes/nagios
install -m 755 check_nagios %{buildroot}/%{_libexecdir}/argo/probes/nagios/check_nagios

%files
%dir /%{_libexecdir}/argo
%dir /%{_libexecdir}/argo/probes/
%dir /%{_libexecdir}/argo/probes/nagios

%attr(0755,root,root) /%{_libexecdir}/argo/probes/nagios/check_nagios
