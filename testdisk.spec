Summary:	Tool to check and undelete partition
Summary(pl):	Narzedzie sprawdzajace i odzyskujace partycje
Name:		testdisk
Version:	3.11	
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(pl):	Aplikacje/System
Group(pt_BR):	Aplicações/Sistema
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tgz
URL:		http://www.cgsecurity.org/testdisk.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to check and undelete partition Works with the following
partitions:
- FAT12 FAT16 FAT32
- Linux
- Linux SWAP (version 1 and 2)
- NTFS (Windows NT)
- BeFS (BeOS)
- UFS (BSD)
- Netware
- RaiserFS

%description -l pl
Narzedzie sprawdzajace i odzyskujace partycje Pracuje z partycjami:
- FAT12 FAT16 FAT32
- Linux
- Linux SWAP (version 1 and 2)
- NTFS (Windows NT)
- BeFS (BeOS)
- UFS (BSD)
- Netware
- RaiserFS

%prep
%setup -q -n %{name}

%build
cd src
%{__make} linux CFLAGS="-I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install src/testdisk	$RPM_BUILD_ROOT%{_sbindir}/
gzip -9nf [L-T]*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/testdisk
