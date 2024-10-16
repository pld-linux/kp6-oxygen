#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.2.1
%define		qtver		5.15.2
%define		kpname		oxygen
Summary:	Plasma and Qt widget style and window decorations for Plasma 5 and KDE 4
Name:		kp6-%{kpname}
Version:	6.2.1
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	75fad24c3ae4437ca114b86576532089
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
BuildRequires:	kp6-libplasma-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	kp5-%{kpname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plasma and Qt widget style and window decorations for Plasma 5 and KDE
4 A plugin-based library to create window decorations.

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
%attr(755,root,root) %{_bindir}/oxygen-settings6
%attr(755,root,root) %{_libdir}/liboxygenstyle6.so.*.*
%ghost %{_libdir}/liboxygenstyle6.so.6
%attr(755,root,root) %{_libdir}/liboxygenstyleconfig6.so.*.*
%ghost %{_libdir}/liboxygenstyleconfig6.so.6
%dir %{_libdir}/qt6/plugins/kstyle_config
%attr(755,root,root) %{_libdir}/qt6/plugins/kstyle_config/kstyle_oxygen_config.so
%attr(755,root,root) %{_libdir}/qt6/plugins/org.kde.kdecoration2.kcm/kcm_oxygendecoration.so
%attr(755,root,root) %{_libdir}/qt6/plugins/org.kde.kdecoration2/org.kde.oxygen.so
%attr(755,root,root) %{_libdir}/qt6/plugins/styles/oxygen6.so
%{_desktopdir}/kcm_oxygendecoration.desktop
%{_datadir}/metainfo/org.kde.oxygen.appdata.xml
%dir %{_datadir}/plasma/desktoptheme/oxygen
%{_datadir}/plasma/desktoptheme/oxygen/colors
%dir %{_datadir}/plasma/desktoptheme/oxygen/dialogs
%{_datadir}/plasma/desktoptheme/oxygen/dialogs/background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/metadata.json
%dir %{_datadir}/plasma/desktoptheme/oxygen/opaque
%dir %{_datadir}/plasma/desktoptheme/oxygen/opaque/dialogs
%{_datadir}/plasma/desktoptheme/oxygen/opaque/dialogs/background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/opaque/dialogs/krunner.svgz
%dir %{_datadir}/plasma/desktoptheme/oxygen/opaque/widgets
%{_datadir}/plasma/desktoptheme/oxygen/opaque/widgets/extender-background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/opaque/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/opaque/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/oxygen/plasmarc
%dir %{_datadir}/plasma/desktoptheme/oxygen/widgets
%{_datadir}/plasma/desktoptheme/oxygen/widgets/action-overlays.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/actionbutton.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/analog_meter.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/arrows.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/bar_meter_horizontal.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/bar_meter_vertical.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/branding.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/busywidget.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/button.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/clock.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/containment-controls.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/dragger.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/extender-background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/extender-dragger.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/frame.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/glowbar.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/line.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/lineedit.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/media-delegate.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/monitor.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/pager.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/plot-background.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/scrollbar.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/scrollwidget.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/slider.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/tabbar.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/tasks.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/timer.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/translucentbackground.svgz
%{_datadir}/plasma/desktoptheme/oxygen/widgets/viewitem.svgz
