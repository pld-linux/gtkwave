# TODO: simarama, FsdbReader support? (BR proprietary libs?)
#
# Conditional build:
%bcond_without	gconf	# GConf usage for preferences
#
Summary:	The GTKWave - electronic waveform viewer
Summary(pl.UTF-8):	GTKWave - przeglądarka przebiegów elektronicznych
Name:		gtkwave
Version:	3.3.60
Release:	1
License:	GPL v2+
Group:		Applications/Printing
Source0:	http://gtkwave.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	c6cb20aeb0f7c1ebc2e84403111cb8e1
URL:		http://gtkwave.sourceforge.net/
%{?with_gconf:BuildRequires:	GConf2-devel >= 2.0}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gperf
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	judy-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel >= 8.4
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
Requires(post,postun):	shared-mime-info >= 0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GTKWave electronic waveform viewer.

%description -l pl.UTF-8
GTKWave jest przeglądraką przebiegów elektronicznych.

%prep
%setup -q

%build
%{__aclocal} -I .
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-judy \
	--disable-mime-update \
	%{?with_gconf:--with-gconf} \
	--with-tcl=/usr/lib \
	--with-tk=/usr/lib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# non-themed icons belong to pixmapsdir
%{__mv} $RPM_BUILD_ROOT%{_iconsdir}/*.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.TXT README
%attr(755,root,root) %{_bindir}/evcd2vcd
%attr(755,root,root) %{_bindir}/fst2vcd
%attr(755,root,root) %{_bindir}/fstminer
%attr(755,root,root) %{_bindir}/ghwdump
%attr(755,root,root) %{_bindir}/gtkwave
%attr(755,root,root) %{_bindir}/lxt2miner
%attr(755,root,root) %{_bindir}/lxt2vcd
%attr(755,root,root) %{_bindir}/rtlbrowse
%attr(755,root,root) %{_bindir}/shmidcat
%attr(755,root,root) %{_bindir}/twinwave
%attr(755,root,root) %{_bindir}/vcd2fst
%attr(755,root,root) %{_bindir}/vcd2lxt
%attr(755,root,root) %{_bindir}/vcd2lxt2
%attr(755,root,root) %{_bindir}/vcd2vzt
%attr(755,root,root) %{_bindir}/vermin
%attr(755,root,root) %{_bindir}/vzt2vcd
%attr(755,root,root) %{_bindir}/vztminer
%{_datadir}/%{name}
%{_datadir}/mime/packages/x-gtkwave-extension-*.xml
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/gnome/*x*/mimetypes/gnome-mime-application-vnd.gtkwave-*.png
%{_iconsdir}/gnome/*x*/mimetypes/gtkwave.png
%{_pixmapsdir}/gtkwave*_256x256x32.png
%{_mandir}/man1/evcd2vcd.1*
%{_mandir}/man1/fst2vcd.1*
%{_mandir}/man1/fstminer.1*
%{_mandir}/man1/ghwdump.1*
%{_mandir}/man1/gtkwave.1*
%{_mandir}/man1/lxt2miner.1*
%{_mandir}/man1/lxt2vcd.1*
%{_mandir}/man1/rtlbrowse.1*
%{_mandir}/man1/shmidcat.1*
%{_mandir}/man1/twinwave.1*
%{_mandir}/man1/vcd2fst.1*
%{_mandir}/man1/vcd2lxt.1*
%{_mandir}/man1/vcd2lxt2.1*
%{_mandir}/man1/vcd2vzt.1*
%{_mandir}/man1/vermin.1*
%{_mandir}/man1/vzt2vcd.1*
%{_mandir}/man1/vztminer.1*
%{_mandir}/man5/gtkwaverc.5*
