Summary:	Easy to use template based DVD authoring tool
Summary(pl.UTF-8):	Proste narzędzie do tworzenia DVD oparte na szablonach
Name:		kmediafactory
Version:	0.5.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://kotisivu.dnainternet.fi/damu0/software/kmediafactory/%{name}-%{version}.tar.bz2
# Source0-md5:	8067ad646b5bc25f871d044fa9cb9e21
Patch0:		kde-ac260.patch
Patch1:		kde-ac260-lt.patch
Patch2:		%{name}-am110.patch
Patch3:		%{name}-funcs.patch
URL:		http://kotisivu.dnainternet.fi/damu0/software/kmediafactory/
BuildRequires:	ImageMagick-c++-devel >= 1:6.0
BuildRequires:	boost-filesystem-devel
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel >= 9:3.3.2
BuildRequires:	libdv-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libtheora-devel
BuildRequires:	qt-designer-libs >= 6:3.3.2
BuildRequires:	qt-devel >= 6:3.3.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	xine-lib-devel
BuildRequires:	zip
Requires:	dvdauthor >= 0.6.11
Requires:	mjpegtools
Requires:	toolame
Requires:	xine-ui
Requires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMediafactory is easy to use template based DVD authoring tool. You
can quickly create DVD menus for home videos and TV recordings in
three simple steps.

%description -l pl.UTF-8
KMediaFactory jest łatwym w użyciu narzędziem do tworzenia DVD opartym
na szablonach. Pozwala szybko stworzyć menu DVD do domowych filmów i
nagrań z TV w trzech prostych krokach.

%package devel
Summary:	Header files for kmediafactory
Summary(pl.UTF-8):	Pliki nagłówkowe dla kmediafactory
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files for kmediafactory.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe programu kmediafactory.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal} -I admin
%{__autoconf}
%configure \
	DVDAUTHOR=%{_bindir}/dvdauthor \
	MPEG2ENC=%{_bindir}/mpeg2enc \
	--disable-rpath \
	--enable-shared \
	--disable-static \
	--disable-embedded \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_datadir}/applnk/*/* $RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog CREDITS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/kmfwidgets.so
%{_libdir}/kde3/*.la
%{_libdir}/kde3/plugins/designer/kmfwidgets.la
%{_datadir}/apps/kmediafactory*
%{_datadir}/apps/kmfwidgets
%{_datadir}/servicetypes/*
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_desktopdir}/kde/*
%{_iconsdir}/*/*/*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
