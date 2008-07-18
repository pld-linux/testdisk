Summary:	Tool to check and undelete partition
Summary(fr.UTF-8):	Outil pour vérifier et restorer des partitions
Summary(pl.UTF-8):	Narzędzie sprawdzające i odzyskujące partycje
Summary(ru.UTF-8):	Программа для проверки и восстановления разделов диска
Name:		testdisk
Version:	6.10
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tar.bz2
# Source0-md5:	d3bde0b546d40e029dda4e9861db40ef
Patch0:		%{name}-ac.patch
URL:		http://www.cgsecurity.org/testdisk.html
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRequires:	libewf-devel
BuildRequires:	libjpeg-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	ntfsprogs-devel >= 1.13.1
BuildRequires:	progsreiserfs-devel >= 0.3.1-1.rc8.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to check and undelete partition. Works with the following
partitions:
- DOS/Windows FAT12, FAT16, FAT32
- Linux Ext2, Ext3
- Linux Swap (version 1 and 2)
- Linux RAID
- LVM and LVM2, Linux Logical Volume Manager
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS (Compressed File System)
- HFS and HFS+, Hierarchical File System
- JFS, IBM's Journaled File System
- Netware NSS
- NTFS (Windows NT/2k/XP)
- ReiserFS 3.5, 3.6, 4
- Sun Solaris i386 disklabel
- UFS, UFS2 (Sun/BSD/...)
- XFS, SGI's Journaled File System

%description -l fr.UTF-8
Outil pour vérifier et restorer des partitions. Fonctionne avec les
partitions suivantes:
- DOS/Windows FAT12, FAT16, FAT32
- Linux Ext2, Ext3
- Linux Swap (version 1 and 2)
- Linux RAID
- LVM/LVM2, Linux Logical Volume Manager
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS (Compressed File System)
- HFS/HFS+, Hierarchical File System
- JFS, IBM's Journaled File System
- Netware NSS
- NTFS (Windows NT/2k/XP)
- ReiserFS 3.5, 3.6, 4
- Sun Solaris i386 disklabel
- UFS, UFS2 (Sun/BSD/...)
- XFS, SGI's Journaled File System

%description -l pl.UTF-8
Narzędzie sprawdzające i odzyskujące partycje. Pracuje z partycjami:
- DOS/Windows FAT12, FAT16, FAT32
- Linux Ext2, Ext3
- Linux Swap (version 1 and 2)
- Linux RAID
- LVM i LVM2 - Linux Logical Volume Manager
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS (Compressed File System)
- HFS i HFS+ - Hierarchical File System
- JFS - IBM's Journaled File System
- Netware NSS
- NTFS (Windows NT/2k/XP)
- ReiserFS 3.5, 3.6, 4
- Sun Solaris i386 disklabel
- UFS, UFS2 (Sun/BSD/...)
- XFS - SGI's Journaled File System

%description -l ru.UTF-8
Программа для проверки и восстановления разделов диска. Поддерживает
следующие типы разделов:
- DOS/Windows FAT12, FAT16, FAT32
- Linux Ext2, Ext3
- Linux Swap (version 1 and 2)
- Linux RAID
- LVM/LVM2, Linux Logical Volume Manager
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS (Compressed File System)
- HFS/HFS+, Hierarchical File System
- JFS, IBM's Journaled File System
- Netware NSS
- NTFS (Windows NT/2k/XP)
- ReiserFS 3.5, 3.6, 4
- Sun Solaris i386 disklabel
- UFS, UFS2 (Sun/BSD/...)
- XFS - SGI's Journaled File System

%prep
%setup -q
%patch0 -p1

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
