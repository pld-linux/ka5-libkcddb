%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		libkcddb
Summary:	libkcddb
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	6cf561dc5c851979af695d6dba4ebeeb
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcodecs-devel >= 5.24.0
BuildRequires:	kf5-kconfig-devel >= 5.24.0
BuildRequires:	kf5-kdoctools-devel >= 5.24.0
BuildRequires:	kf5-ki18n-devel >= 5.24.0
BuildRequires:	kf5-kio-devel >= 5.24.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.24.0
BuildRequires:	libmusicbrainz5-devel >= 5.1.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE CDDB library.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
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
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
