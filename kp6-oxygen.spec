#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeplasmaver	6.3.5
%define		qtver		5.15.2
%define		kpname		oxygen
Summary:	Plasma and Qt widget style and window decorations for Plasma 5 and 6
Summary(pl.UTF-8):	Styl Plasmy i widżetów Qt oraz dekoracje okien dla Plasmy 5 i 6
Name:		kp6-%{kpname}
Version:	6.3.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	82ea0985cdd21f1051f5289bb3dea39d
URL:		https://kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	kf6-extra-cmake-modules >= 1.4.0
BuildRequires:	kf6-frameworkintegration-devel
BuildRequires:	kf6-kcompletion-devel
BuildRequires:	kf6-kconfig-devel
BuildRequires:	kf6-kguiaddons-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-kservice-devel
BuildRequires:	kf6-kwidgetsaddons-devel
BuildRequires:	kf6-kwindowsystem-devel
BuildRequires:	kp6-libplasma-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Obsoletes:	kp5-%{kpname} < 6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plasma and Qt widget style and window decorations for Plasma 5 and 6.

%description -l pl.UTF-8
Styl Plasmy i widżetów Qt oraz dekoracje okien dla Plasmy 5 i 6.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kp5-%{kpname}-devel < %{version}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

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
%attr(755,root,root) %{_libdir}/liboxygenstyle6.so.*.*
%ghost %{_libdir}/liboxygenstyle6.so.6
%attr(755,root,root) %{_libdir}/liboxygenstyleconfig6.so.*.*
%ghost %{_libdir}/liboxygenstyleconfig6.so.6
%dir %{_libdir}/qt6/plugins/kstyle_config
%attr(755,root,root) %{_libdir}/qt6/plugins/kstyle_config/kstyle_oxygen_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/org.kde.kdecoration3/org.kde.oxygen.so
%attr(755,root,root) %{_libdir}/qt6/plugins/org.kde.kdecoration3.kcm/kcm_oxygendecoration.so
%attr(755,root,root) %{_libdir}/qt6/plugins/styles/oxygen6.so
%{_datadir}/color-schemes/Oxygen.colors
%{_datadir}/color-schemes/OxygenCold.colors
%{_datadir}/metainfo/org.kde.oxygen.appdata.xml
%{_datadir}/kstyle/themes/oxygen.themerc
%{_datadir}/plasma/desktoptheme/oxygen
%{_datadir}/plasma/look-and-feel/org.kde.oxygen
%{_desktopdir}/kcm_oxygendecoration.desktop
%{_iconsdir}/hicolor/256x256/apps/oxygen-settings.png
%{_iconsdir}/KDE_Classic
%{_iconsdir}/Oxygen_Black
%{_iconsdir}/Oxygen_Blue
%{_iconsdir}/Oxygen_White
%{_iconsdir}/Oxygen_Yellow
%{_iconsdir}/Oxygen_Zion
