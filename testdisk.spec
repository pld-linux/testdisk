# TODO:
# 	use progsreiserfs-devel instead Source1
#
Summary:	Tool to check and undelete partition
Summary(pl):	Narzêdzie sprawdzaj±ce i odzyskuj±ce partycje
Name:		testdisk
Version:	4.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tgz
Source1:	http://reiserfs.linux.kiev.ua/snapshots/progsreiserfs-0.3.1-rc7.tar.gz
Patch0:		%{name}-LIBEXT.patch
URL:		http://www.cgsecurity.org/testdisk.html
BuildRequires:	e2fsprogs-devel
BuildRequires:	ncurses-devel >= 5.2
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
%setup -q -n %{name} -a 1
%patch0 -p1

%build
cd progsreiserfs-0.3.1-rc7
./configure
%{__make}
cd ..

cd src
%{__make} linux \
	CC=%{__cc} \
	CFLAGS="-I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install src/testdisk $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc [L-T]* doc/*.html doc/*.gif
%attr(755,root,root) %{_sbindir}/testdisk
