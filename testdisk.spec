Summary:	Tool to check and undelete partition
Summary(fr.UTF-8):	Outil pour vérifier et restorer des partitions
Summary(pl.UTF-8):	Narzędzie sprawdzające i odzyskujące partycje
Summary(ru.UTF-8):	Программа для проверки и восстановления разделов диска
Name:		testdisk
Version:	6.14
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.cgsecurity.org/%{name}-%{version}.tar.bz2
# Source0-md5:	b1f0edabc9035e9ec9c8e0a95059ff3f
Patch0:		%{name}-ac.patch
URL:		http://www.cgsecurity.org/wiki/TestDisk
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRequires:	libcom_err-devel
#BuildRequires:	libcarvpath-devel
BuildRequires:	libewf-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libuuid-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	ntfs-3g-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	progsreiserfs-devel >= 0.3.1-1.rc8.1
BuildRequires:	zlib-devel
Requires:	uname(release) >= 2.6.18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to check and undelete partition. Works with the following
partitions:
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS, Compressed File System
- DOS/Windows FAT12, FAT16 and FAT32
- Windows exFAT
- HFS, HFS+ and HFSX, Hierarchical File System
- JFS, IBM's Journaled File System
- Linux ext2/ext3/ext4
- Linux LUKS encrypted partition
- Linux RAID md 0.9/1.0/1.1/1.2 o RAID 1: mirroring o RAID 4: striped
  array with parity device o RAID 5: striped array with distributed
  parity information o RAID 6: striped array with distributed dual
  redundancy information
- Linux Swap (versions 1 and 2)
- LVM and LVM2, Linux Logical Volume Manager
- Mac partition map
- Novell Storage Services NSS
- NTFS (Windows NT/2000/XP/2003/Vista/2008 )
- ReiserFS 3.5, 3.6 and 4
- Sun Solaris i386 disklabel
- Unix File System UFS and UFS2 (Sun/BSD/...)
- XFS, SGI's Journaled File System

%description -l fr.UTF-8
Outil pour vérifier et restorer des partitions. Fonctionne avec les
partitions suivantes:
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS, Compressed File System
- DOS/Windows FAT12, FAT16 and FAT32
- Windows exFAT
- HFS, HFS+ and HFSX, Hierarchical File System
- JFS, IBM's Journaled File System
- Linux ext2/ext3/ext4
- Linux LUKS encrypted partition
- Linux RAID md 0.9/1.0/1.1/1.2 o RAID 1: mirroring o RAID 4: striped
  array with parity device o RAID 5: striped array with distributed
  parity information o RAID 6: striped array with distributed dual
  redundancy information
- Linux Swap (versions 1 and 2)
- LVM and LVM2, Linux Logical Volume Manager
- Mac partition map
- Novell Storage Services NSS
- NTFS (Windows NT/2000/XP/2003/Vista/2008)
- ReiserFS 3.5, 3.6 and 4
- Sun Solaris i386 disklabel
- Unix File System UFS and UFS2 (Sun/BSD/...)
- XFS, SGI's Journaled File System

%description -l pl.UTF-8
Narzędzie sprawdzające i odzyskujące partycje. Pracuje z partycjami:
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS, Compressed File System
- DOS/Windows FAT12, FAT16 and FAT32
- Windows exFAT
- HFS, HFS+ and HFSX, Hierarchical File System
- JFS, IBM's Journaled File System
- Linux ext2/ext3/ext4
- Linux LUKS encrypted partition
- Linux RAID md 0.9/1.0/1.1/1.2 o RAID 1: mirroring o RAID 4: striped
  array with parity device o RAID 5: striped array with distributed
  parity information o RAID 6: striped array with distributed dual
  redundancy information
- Linux Swap (versions 1 and 2)
- LVM and LVM2, Linux Logical Volume Manager
- Mac partition map
- Novell Storage Services NSS
- NTFS (Windows NT/2000/XP/2003/Vista/2008)
- ReiserFS 3.5, 3.6 and 4
- Sun Solaris i386 disklabel
- Unix File System UFS and UFS2 (Sun/BSD/...)
- XFS, SGI's Journaled File System

%description -l ru.UTF-8
Программа для проверки и восстановления разделов диска. Поддерживает
следующие типы разделов:
- BeFS (BeOS)
- BSD disklabel (FreeBSD/OpenBSD/NetBSD)
- CramFS, Compressed File System
- DOS/Windows FAT12, FAT16 and FAT32
- Windows exFAT
- HFS, HFS+ and HFSX, Hierarchical File System
- JFS, IBM's Journaled File System
- Linux ext2/ext3/ext4
- Linux LUKS encrypted partition
- Linux RAID md 0.9/1.0/1.1/1.2 o RAID 1: mirroring o RAID 4: striped
  array with parity device o RAID 5: striped array with distributed
  parity information o RAID 6: striped array with distributed dual
  redundancy information
- Linux Swap (versions 1 and 2)
- LVM and LVM2, Linux Logical Volume Manager
- Mac partition map
- Novell Storage Services NSS
- NTFS (Windows NT/2000/XP/2003/Vista/2008)
- ReiserFS 3.5, 3.6 and 4
- Sun Solaris i386 disklabel
- Unix File System UFS and UFS2 (Sun/BSD/...)
- XFS, SGI's Journaled File System

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
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install -p src/{fidentify,photorec,testdisk} $RPM_BUILD_ROOT%{_sbindir}
cp -p doc_src/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INFO NEWS README THANKS *.html
%attr(755,root,root) %{_sbindir}/fidentify
%attr(755,root,root) %{_sbindir}/photorec
%attr(755,root,root) %{_sbindir}/testdisk
%{_mandir}/man8/fidentify.8*
%{_mandir}/man8/photorec.8*
%{_mandir}/man8/testdisk.8*
