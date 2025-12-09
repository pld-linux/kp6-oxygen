#
# Conditional build:
%bcond_with	tests		# test suite

%define		kf_ver		6.10.0
%define		kp_ver		%{version}
%define		qt_ver		6.7.0
%define		kpname		oxygen
Summary:	Plasma and Qt widget style and window decorations for Plasma 5 and 6
Summary(pl.UTF-8):	Styl Plasmy i widżetów Qt oraz dekoracje okien dla Plasmy 5 i 6
Name:		kp6-%{kpname}
Version:	6.5.4
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{version}/%{kpname}-%{version}.tar.xz
# Source0-md5:	914f568d9e945539014d8dbe285fade6
URL:		https://kde.org/
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6DBus-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
BuildRequires:	Qt6Network-devel >= %{qt_ver}
BuildRequires:	Qt6OpenGL-devel >= %{qt_ver}
BuildRequires:	Qt6Quick-devel >= %{qt_ver}
BuildRequires:	Qt6Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.25
BuildRequires:	kf6-extra-cmake-modules >= 5.102.0
BuildRequires:	kf6-frameworkintegration-devel >= %{kf_ver}
BuildRequires:	kf6-kcmutils-devel >= %{kf_ver}
BuildRequires:	kf6-kcolorscheme-devel >= %{kf_ver}
BuildRequires:	kf6-kcompletion-devel >= %{kf_ver}
BuildRequires:	kf6-kconfig-devel >= %{kf_ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kguiaddons-devel >= %{kf_ver}
BuildRequires:	kf6-ki18n-devel >= %{kf_ver}
BuildRequires:	kf6-kservice-devel >= %{kf_ver}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kp6-kdecoration-devel >= %{kp_ver}
BuildRequires:	kp6-libplasma-devel >= %{kp_ver}
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires:	Qt6DBus >= %{qt_ver}
Requires:	Qt6Gui >= %{qt_ver}
Requires:	Qt6Quick >= %{qt_ver}
Requires:	Qt6Widgets >= %{qt_ver}
Requires:	kf6-frameworkintegration >= %{kf_ver}
Requires:	kf6-kcmutils >= %{kf_ver}
Requires:	kf6-kcolorscheme >= %{kf_ver}
Requires:	kf6-kcompletion >= %{kf_ver}
Requires:	kf6-kconfig >= %{kf_ver}
Requires:	kf6-kcoreaddons >= %{kf_ver}
Requires:	kf6-kguiaddons >= %{kf_ver}
Requires:	kf6-ki18n >= %{kf_ver}
Requires:	kf6-kwidgetsaddons >= %{kf_ver}
Requires:	kf6-kwindowsystem >= %{kf_ver}
Requires:	kp6-kdecoration >= %{kp_ver}
Requires:	kp6-libplasma >= %{kp_ver}
%requires_eq_to Qt6Core Qt6Core-devel
Provides:	kf5-plasma-desktoptheme-oxygen = %{version}-%{release}
Obsoletes:	kf5-plasma-desktoptheme-oxygen < 6
Obsoletes:	kp5-oxygen < 6
Conflicts:	kf5-plasma-framework < 5.116.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plasma and Qt widget style and window decorations for Plasma 5 and 6.

%description -l pl.UTF-8
Styl Plasmy i widżetów Qt oraz dekoracje okien dla Plasmy 5 i 6.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DBUILD_QT5=OFF \
	-DBUILD_QT6=ON

%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post

%postun
/sbin/ldconfig
%update_desktop_database_postun

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oxygen-demo6
%attr(755,root,root) %{_bindir}/oxygen-settings6
%{_libdir}/liboxygenstyle6.so.*.*
%ghost %{_libdir}/liboxygenstyle6.so.6
%{_libdir}/liboxygenstyleconfig6.so.*.*
%ghost %{_libdir}/liboxygenstyleconfig6.so.6
%dir %{_libdir}/qt6/plugins/kstyle_config
%{_libdir}/qt6/plugins/kstyle_config/kstyle_oxygen_config.so
%{_libdir}/qt6/plugins/org.kde.kdecoration3/org.kde.oxygen.so
%{_libdir}/qt6/plugins/org.kde.kdecoration3.kcm/kcm_oxygendecoration.so
%{_libdir}/qt6/plugins/styles/oxygen6.so
%{_datadir}/color-schemes/Oxygen.colors
%{_datadir}/color-schemes/OxygenCold.colors
%{_datadir}/metainfo/org.kde.oxygen.appdata.xml
%{_datadir}/kstyle/themes/oxygen.themerc
%{_datadir}/plasma/desktoptheme/oxygen
%{_datadir}/plasma/look-and-feel/org.kde.oxygen
%{_desktopdir}/kcm_oxygendecoration.desktop
%{_iconsdir}/KDE_Classic
%{_iconsdir}/Oxygen_Black
%{_iconsdir}/Oxygen_Blue
%{_iconsdir}/Oxygen_White
%{_iconsdir}/Oxygen_Yellow
%{_iconsdir}/Oxygen_Zion
%{_iconsdir}/hicolor/256x256/apps/oxygen-settings.png
