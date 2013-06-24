Summary:	The GTKWave - electronic waveform viewer
Summary(pl.UTF-8):	The GTKWave - przeglądarka przebiegów elektronicznych
Name:		gtkwave
Version:	3.3.47
Release:	1
License:	GPL
Group:		Applications/Printing
Source0:	http://gtkwave.sourceforge.net/%{name}-%{version}.tar.gz
# Source0-md5:	fdb257ed42220a9a7526b70d1746054a
URL:		http://gtkwave.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	judy-devel
BuildRequires:	libtool
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	xz-devel
Requires(post,postun):	shared-mime-info >= 0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GTKWave electronic waveform viewer.

%description -l pl.UTF-8
The GTKWave jest przeglądraką przebiegów elektronicznych.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I .
%{__automake}
%{__autoconf}
%configure \
	UPDATE_DESKTOP_DATABASE=/bin/true \
	--enable-judy \
	--with-tcl=/usr/lib \
	--with-tk=/usr/lib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc ANALOG_README.TXT SYSTEMVERILOG_README.TXT
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/mime/application/*.xml
%{_datadir}/mime/packages/*.xml
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/gnome/*/*/*.png
%{_iconsdir}/*.png
%{_mandir}/*/*
