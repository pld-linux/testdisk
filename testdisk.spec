Summary:	Tool to check and undelete partition
Summary(pl):	Narzêdzie sprawdzaj±ce i odzyskuj±ce partycje
Name:		testdisk
Version:	4.5
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tar.gz
# Source0-md5:	6f2687efb3657f6ae797cdc04ff8b7fc
Patch0:		%{name}-LIBEXT.patch
Patch1:		%{name}-va.patch
URL:		http://www.cgsecurity.org/testdisk.html
BuildRequires:	e2fsprogs-devel
BuildRequires:	ncurses-devel >= 5.2
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
%patch0 -p1
%patch1 -p1

%build
%{__make} -C src linux \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install src/testdisk $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO doc/*.html doc/*.gif
%attr(755,root,root) %{_sbindir}/testdisk
