Summary:	Tool to check and undelete partition
Summary(pl):	Narzêdzie sprawdzaj±ce i odzyskuj±ce partycje
Name:		testdisk
Version:	5.8
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tar.gz
# Source0-md5:	629e035e0ded72388df30f3c743d7a83
URL:		http://www.cgsecurity.org/testdisk.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	ntfsprogs-devel >= 1.9.4 
BuildRequires:	progsreiserfs-devel >= 0.3.1-1.rc8.1
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
Narzêdzie sprawdzaj±ce i odzyskuj±ce partycje. Pracuje z partycjami:
- FAT12 FAT16 FAT32
- Linux
- Linux SWAP (version 1 and 2)
- NTFS (Windows NT)
- BeFS (BeOS)
- UFS (BSD)
- Netware
- ReiserFS

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install src/testdisk $RPM_BUILD_ROOT%{_sbindir}
install src/photorec $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INFO NEWS README THANKS doc/*.html doc/*.gif
%attr(755,root,root) %{_sbindir}/*
