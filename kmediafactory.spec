Summary:	Easy to use template based DVD authoring tool
Summary(pl):	Proste narz�dzie do tworzenia DVD oparte na szablonach
Name:		kmediafactory
Version:	0.4.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://susku.pyhaselka.fi/damu/software/kmediafactory/%{name}-%{version}.tar.bz2
# Source0-md5:	a51d5b6a0a5d9f0dcf819b6f81dc2e83
URL:		http://susku.pyhaselka.fi/damu/software/kmediafactory/
BuildRequires:	ImageMagick-c++-devel >= 1:6.0
BuildRequires:	dvdauthor >= 0.6.11
BuildRequires:	kdebase-devel >= 9:3.3
BuildRequires:	mjpegtools
BuildRequires:	qt-devel >= 6:3.3.2
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	toolame
Requires:	xine-ui
Requires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Patch:		%{name}-includehints.pach

%description
KMediafactory is easy to use template based DVD authoring tool. You
can quickly create DVD menus for home videos and TV recordings in
three simple steps.

%description -l pl
KMediaFactory jest �atwym w u�yciu narz�dziem do tworzenia DVD opartym
na szablonach. Pozwala szybko stworzy� menu DVD do domowych film�w i
nagra� z TV w trzech prostych krokach.

%package devel
Summary:	Header files for kmediafactory
Summary(pl):	Pliki nag��wkowe dla kmediafactory
Group:		Development/Tools

%description devel
This package contains header files for kmediafactory.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe programu kmediafactory.

%prep
%setup -q
%patch -p1

%build
%configure
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
%{_iconsdir}/*/*/*/*
%{_datadir}/servicetypes/*
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_datadir}/apps/*
%{_desktopdir}/kde/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/kmfwidgets.so
%{_libdir}/kde3/*.la
%{_libdir}/kde3/plugins/designer/kmfwidgets.la
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
