Summary:	Tool to check and undelete partition
Summary(pl):	Narzêdzie sprawdzaj±ce i odzyskuj±ce partycje
Name:		testdisk
Version:	4.1
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tgz
Patch0:		%{name}-va_arg.patch
URL:		http://www.cgsecurity.org/testdisk.html
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	e2fsprogs-devel
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
- ReiserFS

%description -l pl
Narzêdzie sprawdzaj±ce i odzyskujace partycje. Pracuje z partycjami:
- FAT12 FAT16 FAT32
- Linux
- Linux SWAP (version 1 and 2)
- NTFS (Windows NT)
- BeFS (BeOS)
- UFS (BSD)
- Netware
- ReiserFS

%prep
%setup -q -n %{name}
%patch0 -p0

%build
cd src
%{__make} linux \
	CC=%{__cc} \
	CFLAGS="-I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install src/testdisk	$RPM_BUILD_ROOT%{_sbindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc [L-T]* doc/*.html doc/*.gif
%attr(755,root,root) %{_sbindir}/testdisk
