%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		libkcddb
Summary:	libkcddb
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ed8176aac99d3ccf0bfa330462fd1c86
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	libmusicbrainz5-devel >= 5.1.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libkccdb.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libKF5Cddb.so.5
%attr(755,root,root) %{_libdir}/libKF5Cddb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5CddbWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5CddbWidgets.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_cddb.so
%{_datadir}/config.kcfg/libkcddb5.kcfg
%{_datadir}/kservices5/libkcddb.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KCddb
%{_includedir}/KF5/kcddb_version.h
%{_libdir}/cmake/KF5Cddb
%attr(755,root,root) %{_libdir}/libKF5Cddb.so
%attr(755,root,root) %{_libdir}/libKF5CddbWidgets.so
%{_libdir}/qt5/mkspecs/modules/qt_KCddb.pri
