Summary:	Tool to check and undelete partition
Summary(fr):	Outil pour v�rifier et restorer des partitions
Summary(pl):	Narz�dzie sprawdzaj�ce i odzyskuj�ce partycje
Summary(ru):	��������� ��� �������� � �������������� �������� �����
Name:		testdisk
Version:	6.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tar.bz2
# Source0-md5:	188c2216c76f2fe4db8eae1ea033188a
URL:		http://www.cgsecurity.org/testdisk.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	ntfsprogs-devel >= 1.13.1
BuildRequires:	progsreiserfs-devel >= 0.3.1-1.rc8.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to check and undelete partition. Works with the following
partitions:
- FAT12 FAT16 FAT32
- Linux Ext2, Ext3
- Linux SWAP (version 1 and 2)
- Linux Raid
- LVM and LVM2, Linux Logical Volume Manager
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS (Compressed File System)
- HFS, Hierarchical File System
- JFS, IBM's Journaled File System
- Netware NSS
- NTFS (Windows NT/2k/XP)
- ReiserFS 3.5, 3.6
- UFS (Sun/BSD)
- XFS

%description -l fr
Outil pour v�rifier et restorer des partitions. Fonctionne avec les
partitions suivantes:
- FAT12 FAT16 FAT32
- Linux Ext2, Ext3
- Linux SWAP (version 1 and 2)
- Linux Raid
- LVM and LVM2, Linux Logical Volume Manager
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS (Compressed File System)
- HFS, Hierarchical File System
- JFS, IBM's Journaled File System
- Netware NSS
- NTFS (Windows NT/2k/XP)
- ReiserFS 3.5, 3.6
- UFS (Sun/BSD)
- XFS

%description -l pl
Narz�dzie sprawdzaj�ce i odzyskuj�ce partycje. Pracuje z partycjami:
- FAT12 FAT16 FAT32
- Linux Ext2, Ext3
- Linux SWAP (version 1 and 2)
- Linux Raid
- LVM and LVM2, Linux Logical Volume Manager
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS (Compressed File System)
- HFS, Hierarchical File System
- JFS, IBM's Journaled File System
- Netware NSS
- NTFS (Windows NT/2k/XP)
- ReiserFS 3.5, 3.6
- UFS (Sun/BSD)
- XFS

%description -l ru
��������� ��� �������� � �������������� �������� �����. ������������
��������� ���� ��������:
- FAT12 FAT16 FAT32
- Linux Ext2, Ext3
- Linux SWAP (version 1 and 2)
- Linux Raid
- LVM and LVM2, Linux Logical Volume Manager
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS (Compressed File System)
- HFS, Hierarchical File System
- JFS, IBM's Journaled File System
- Netware NSS
- NTFS (Windows NT/2k/XP)
- ReiserFS 3.5, 3.6
- UFS (Sun/BSD)
- XFS

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
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install src/testdisk $RPM_BUILD_ROOT%{_sbindir}
install src/photorec $RPM_BUILD_ROOT%{_sbindir}
install doc_src/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INFO NEWS README THANKS doc/*.html doc/*.gif
%{_mandir}/man1/*.1*
%attr(755,root,root) %{_sbindir}/*
