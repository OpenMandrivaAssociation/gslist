%define	name	gslist
%define	version	0.8.1
%define	release	1

Summary:	Gslist is a command-line game servers browser and heartbeats sender
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Group:		Networking/Other
License:	GPL
URL:		http://aluigi.altervista.org/papers.htm#gslist
Source0:	%{name}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Gslist is a command-line game servers browser and heartbeats sender,
it supports an incredible amount of games and moreover a lot of
options making it simple and complete at the same time.
It can run a specific application for each gameserver,
can request informations, lets you to filter the servers list
(for country, gamename, port, number of players...) and more.

%prep
%setup -n %{name}
chmod 644 gslist.txt

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc gslist.txt
%{_bindir}/%{name}

