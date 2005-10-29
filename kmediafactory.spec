Summary:	Easy to use template based DVD authoring tool
Summary(pl):	Proste narzêdzie do tworzenia DVD oparte na szablonach
Name:		kmediafactory
Version:	0.4.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://susku.pyhaselka.fi/damu/software/kmediafactory/%{name}-%{version}.tar.bz2
# Source0-md5:	8acea22f25bb24e829c6b04b64126d29
Patch0:		%{name}-includehints.pach
URL:		http://susku.pyhaselka.fi/damu/software/kmediafactory/
BuildRequires:	ImageMagick-c++-devel >= 1:6.0
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel >= 9:3.3
BuildRequires:	libdv-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libtheora-devel
BuildRequires:	qt-devel >= 6:3.3.2
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	xine-lib-devel
BuildRequires:	zip
Requires:	dvdauthor < 0.6.11
Requires:	toolame
Requires:	xine-ui
Requires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMediafactory is easy to use template based DVD authoring tool. You
can quickly create DVD menus for home videos and TV recordings in
three simple steps.

%description -l pl
KMediaFactory jest ³atwym w u¿yciu narzêdziem do tworzenia DVD opartym
na szablonach. Pozwala szybko stworzyæ menu DVD do domowych filmów i
nagrañ z TV w trzech prostych krokach.

%package devel
Summary:	Header files for kmediafactory
Summary(pl):	Pliki nag³ówkowe dla kmediafactory
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files for kmediafactory.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe programu kmediafactory.

%prep
%setup -q
%patch0 -p1

#sed -i -e 's,/lib\>,/%{_lib},' admin/{dv,dvdread,fontconfig,theora,xine}.m4
sed -i -e 's,/lib\>,/%{_lib},' configure

%build
%configure \
	DVDAUTHOR=/usr/bin/dvdauthor \
	MPEG2ENC=/usr/bin/mpeg2enc \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_datadir}/applnk/*/* $RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --with-kde

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
