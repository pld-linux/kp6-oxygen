#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.0.1
%define		qtver		5.15.2
%define		kpname		oxygen
Summary:	Plasma and Qt widget style and window decorations for Plasma 5 and KDE 4
Name:		kp6-%{kpname}
Version:	6.0.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	26e07aa7df139240fc5060e6e0e08293
URL:		http://www.kde.org/
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
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plasma and Qt widget style and window decorations for Plasma 5 and KDE
4 A plugin-based library to create window decorations.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%{_datadir}/plasma/look-and-feel/org.kde.oxygen
%{_iconsdir}/KDE_Classic
%{_datadir}/kstyle/themes/oxygen.themerc
%{_iconsdir}/hicolor/256x256/apps/oxygen-settings.png
%{_iconsdir}/Oxygen*
%{_datadir}/color-schemes/Oxygen.colors
%{_datadir}/color-schemes/OxygenCold.colors
%attr(755,root,root) %{_bindir}/oxygen-demo6
%attr(755,root,root)%{_bindir}/oxygen-settings6
%attr(755,root,root)%{_libdir}/liboxygenstyle6.so.*.*
%ghost %{_libdir}/liboxygenstyle6.so.6
%attr(755,root,root)%{_libdir}/liboxygenstyleconfig6.so.*.*
%ghost %{_libdir}/liboxygenstyleconfig6.so.6
%attr(755,root,root)%{_libdir}/qt6/plugins/kstyle_config/kstyle_oxygen_config.so
%attr(755,root,root)%{_libdir}/qt6/plugins/org.kde.kdecoration2.kcm/kcm_oxygendecoration.so
%attr(755,root,root)%{_libdir}/qt6/plugins/org.kde.kdecoration2/org.kde.oxygen.so
%attr(755,root,root)%{_libdir}/qt6/plugins/styles/oxygen6.so
%{_desktopdir}/kcm_oxygendecoration.desktop
%{_datadir}/metainfo/org.kde.oxygen.appdata.xml
