Summary:	Easy to use template based dvd authoring tool
Summary(pl):	Proste narzêdzie oparte na szablonach dvd
Name:		kmediafactory
Version:	0.3.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://susku.pyhaselka.fi/damu/software/kmediafactory/%{name}-%{version}.tar.bz2
# Source0-md5:	a2901674bc558112837e356e45b93a5a
URL:		http://susku.pyhaselka.fi/damu/software/kmediafactory/
BuildRequires:	ImageMagick-devel >= 1:6.0
BuildRequires:	dvdauthor >= 0.6.11
BuildRequires:	qt-devel >= 6:3.3.2
BuildRequires:	kdebase-devel >= 9:3.3
BuildRequires:	mjpegtools
Requires:	toolame
Requires:	xine
Requires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMediafactory is easy to use template based dvd authoring tool. You
can quickly create DVD menus for home videos and TV recordings in
three simple steps.

%description -l pl
KMediaFactory jest ³atwym w u¿yciu narzêdziem opartym na szablonach
dvd. Mo¿esz szybko stworzyæ menu dvd do domowych filmów i nagrywaæ tv
w trzech prostych krokach.

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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README COPYING LICENSE
%{_bindir}/*
%{_libdir}/kde3/*
%{_libdir}/lib*.so.*.*
%{_datadir}/applnk/Utilities/*
%{_datadir}/apps/kmediafactory/*
%{_datadir}/apps/kmediafactory_output/*
%{_datadir}/apps/kmediafactory_template/*
%{_datadir}/apps/kmediafactory_video/*
%{_datadir}/doc/HTML/en/kmediafactory/*
%{_datadir}/doc/HTML/en/kmediafactory/index.cache.bz2
%{_datadir}/doc/HTML/en/kmediafactory/index.docbook
%{_datadir}/doc/HTML/en/kmediafactory/index.docbook.orig
%{_datadir}/icons/crystalsvg/128x128/apps/kmediafactory.png
%{_datadir}/icons/crystalsvg/128x128/mimetypes/kmediafactory_project.png
%{_datadir}/icons/crystalsvg/16x16/apps/kmediafactory.png
%{_datadir}/icons/crystalsvg/16x16/mimetypes/kmediafactory_project.png
%{_datadir}/icons/crystalsvg/22x22/apps/kmediafactory.png
%{_datadir}/icons/crystalsvg/22x22/mimetypes/kmediafactory_project.png
%{_datadir}/icons/crystalsvg/32x32/actions/add_video.png
%{_datadir}/icons/crystalsvg/32x32/apps/kmediafactory.png
%{_datadir}/icons/crystalsvg/32x32/mimetypes/kmediafactory_project.png
%{_datadir}/icons/crystalsvg/48x48/apps/kmediafactory.png
%{_datadir}/icons/crystalsvg/48x48/mimetypes/kmediafactory_project.png
%{_datadir}/icons/crystalsvg/64x64/apps/kmediafactory.png
%{_datadir}/icons/crystalsvg/64x64/mimetypes/kmediafactory_project.png
%{_datadir}/icons/crystalsvg/scalable/apps/kmediafactory.svgz
%{_datadir}/icons/crystalsvg/scalable/mimetypes/kmediafactory_project.svgz
%{_datadir}/mimelnk/application/x-kmediafactory.desktop
%{_datadir}/services/kmediafactory_output.desktop
%{_datadir}/services/kmediafactory_template.desktop
%{_datadir}/services/kmediafactory_video.desktop
%{_datadir}/servicetypes/kmediafactoryplugin.desktop 

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/*.h
