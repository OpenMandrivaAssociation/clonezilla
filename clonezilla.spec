Summary:	Opensource Clone System (ocs), clonezilla
Name:		clonezilla
Version:	5.5.20
Release:	1
License:	GPLv2+
Group:		Archiving/Backup
URL:		http://www.clonezilla.org
Source0:	http://free.nchc.org.tw/drbl-core/src/unstable/%{name}-%{version}.tar.xz
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
%setup -q

%build
%make_build

%install
%make_install

%files
%doc doc/*
%_sbindir/*
%_bindir/*
%_datadir/drbl/*
%_datadir/%name/
%_sysconfdir/drbl/*
