Summary:	Opensource Clone System (ocs), clonezilla
Name:		clonezilla
Version:	5.6.23
Release:	1
License:	GPLv2+
Group:		Archiving/Backup
URL:		http://www.clonezilla.org
Source0:	http://free.nchc.org.tw/drbl-core/src/unstable/%{name}-%{version}.tar.xz
Patch0:   usrbin.patch  
BuildArch:	noarch
Requires:	drbl
Requires:	partimage
Requires:	psmisc
Requires:	udpcast
Requires:	partclone
Requires:	ntfsprogs
Requires:	dialog

%description
Clonezilla, based on DRBL, Partition Image, ntfsclone, partclone, and udpcast,
allows you to do bare metal backup and recovery. Two types of Clonezilla
are available, Clonezilla live and Clonezilla SE (Server Edition). Clonezilla
live is suitable for single machine backup and restore. While Clonezilla SE
is for massive deployment, it can clone many (40 plus!) computers simultaneously.
For more info, check http://clonezilla.org, http://clonezilla.nchc.org.tw.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install

%files
%doc doc/*
%{_bindir}/clonezilla
%{_bindir}/cnvt-ocs-dev
%{_bindir}/create-debian-live
%{_bindir}/create-drbl-live
%{_bindir}/create-drbl-live-by-pkg
%{_bindir}/create-gparted-live
%{_bindir}/create-ocs-tmp-img
%{_bindir}/create-ubuntu-live
%{_bindir}/cv-ocsimg-v1-to-v2
%{_bindir}/drbl-ocs
%{_bindir}/drbl-ocs-live-prep
%{_bindir}/ocs-*
%{_bindir}/ocsmgrd
%{_bindir}/prep-ocsroot
%{_bindir}/update-efi-nvram-boot-entry
%{_bindir}/gen-torrent-from-ptcl
%{_bindir}/get-latest-ocs-live-ver
%_datadir/drbl/*
%_datadir/%name/
%_sysconfdir/drbl/*
