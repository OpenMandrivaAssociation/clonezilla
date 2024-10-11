Summary:	Opensource Clone System (ocs), clonezilla
Name:		clonezilla
Version:	5.6.23
Release:	1
License:	GPLv2+
Group:		Archiving/Backup
URL:		http://www.clonezilla.org
Source0:	http://free.nchc.org.tw/drbl-core/src/unstable/%{name}-%{version}.tar.xz
#Patch0:   usrbin.patch  
BuildArch:	noarch
Requires:	drbl
Requires:	partimage
Requires:	psmisc
Requires:	udpcast
Requires:	partclone
Requires:	ntfsprogs
Requires:	cdialog

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
#{_sbindir}/clonezilla
#{_sbindir}/nvt-ocs-dev
#{_sbindir}/create-debian-live
#{_sbindir}/create-drbl-live
#{_sbindir}/create-drbl-live-by-pkg
#{_sbindir}/create-gparted-live
#{_sbindir}/create-ocs-tmp-img
#{_sbindir}/create-ubuntu-live
#{_sbindir}/cv-ocsimg-v1-to-v2
#{_sbindir}/drbl-ocs
#{_sbindir}/drbl-ocs-live-prep
#{_sbindir}/ocs-*
#{_sbindir}/ocsmgrd
#{_sbindir}/prep-ocsroot
#{_sbindir}/update-efi-nvram-boot-entry
%{_bindir}/gen-torrent-from-ptcl
%{_bindir}/get-latest-ocs-live-ver
%{_bindir}/ocs-get-nic-fw-lst
%{_bindir}/ocs-live-ver
%{_bindir}/ocs-scan-disk
%{_bindir}/ocs-socket
%_datadir/drbl/*
%_datadir/%name/
%_sysconfdir/drbl/*
