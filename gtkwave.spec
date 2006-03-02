Summary:	The GTKWave - electronic waveform viewer
Summary(pl):	The GTKWave - przegl�darka przebieg�w elektronicznych
Name:		gtkwave
Version:	2.0.0pre5
Release:	1
License:	GPL
Group:		Applications/Printing
Source0:	ftp://ftp.cs.man.ac.uk/pub/amulet/gtkwave/2.0/%{name}-%{version}.tar.gz
# Source0-md5:	d1837e53b933643e0b6c6a6527022907
Patch0:		%{name}-xml.patch
URL:		http://www.cs.manchester.ac.uk/apt/projects/tools/gtkwave/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	bzip2-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libxml2-devel >= 2.6.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GTKWave electronic waveform viewer.

%description -l pl
The GTKWave jest przegl�drak� przebieg�w elektronicznych.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtkwave/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gtkwave/*.so*
# .la are required
%{_libdir}/gtkwave/*.la
%{_datadir}/gtkwave