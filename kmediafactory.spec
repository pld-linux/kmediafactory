Summary:	Easy to use template based dvd authoring tool
Summary(pl):	Proste narzêdzie oparte na szablonach dvd
Name:		kmediafactory
Version:	0.3.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://susku.pyhaselka.fi/damu/software/kmediafactory/%{name}-%{version}.tar.bz2
# Source0-md5:	e61efce22161907449b07f8472eb7c7c
URL:		http://susku.pyhaselka.fi/damu/software/kmediafactory/
BuildRequires:	ImageMagick-devel >= 6.0
BuildRequires:	dvdauthor >= 0.6.11
BuildRequires:	libdv-devel
BuildRequires:	mjpegtools
Requires:	toolame
Requires:	xine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMediafactory is easy to use template based dvd authoring tool. You can quickly create DVD menus for home videos and TV recordings in three simple steps.

%description -l pl
KMediaFactory jest ³atwym w u¿yciu narzêdziem opartym na szablonach dvd. Mo¿esz szybko stworzyæ menu dvd do domowych filmów i nagrywaæ tv w trzech prostych krokach.

%package devel
Summary:	Header files for kmediafactory
Summary(pl):	Pliki nag³ówkowe dla kmediafactory
Group:		Development/Tools	

%description devel
This package contains header files for kmediafactory

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe programu kmediafactory

%prep
%setup -q

%configure

%build
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/%{_datadir}

%{__make} install 

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README COPYING LICENSE
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_datadir}/*
%attr(755,root,root) %{_includedir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/kmediafactory
