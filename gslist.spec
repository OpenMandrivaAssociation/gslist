%define	name	gslist
%define	version	0.8.10d
%define	release	1

Summary:	Gslist is a command-line game servers browser and heartbeats sender
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Group:		Networking/Other
License:	GPL
URL:		http://aluigi.altervista.org/papers.htm#gslist
Source0:	%{name}.zip
source1:	.abf.yml
patch0:		gslist-0.8.10d.fixmake.patch
buildrequires:	GeoIP-devel
buildrequires:	mysql-devel

%description
Gslist is a command-line game servers browser and heartbeats sender,
it supports an incredible amount of games and moreover a lot of
options making it simple and complete at the same time.
It can run a specific application for each gameserver,
can request informations, lets you to filter the servers list
(for country, gamename, port, number of players...) and more.

%prep
%setup -c %{name}
%patch0 -p1 -b .fixmake

%build
make clean
%make CFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall_std PREFIX=%{buildroot}%{_prefix}

%files
%defattr(-,root,root)
%doc gslist.txt
%{_bindir}/%{name}
%{_bindir}/%{name}sql



%changelog
* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.8.1-1mdv2008.1
+ Revision: 126343
- kill re-definition of %%buildroot on Pixel's request
- import gslist


* Tue Mar 28 2006 Jerome Soyer <saispo@mandriva.org> 0.8.1-1mdk
- New release 0.8.1

* Wed Jul 27 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.6.3-1mdk
- inital release (club request)
