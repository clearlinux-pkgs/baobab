#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : baobab
Version  : 40.0
Release  : 19
URL      : https://download.gnome.org/sources/baobab/40/baobab-40.0.tar.xz
Source0  : https://download.gnome.org/sources/baobab/40/baobab-40.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0
Requires: baobab-bin = %{version}-%{release}
Requires: baobab-data = %{version}-%{release}
Requires: baobab-license = %{version}-%{release}
Requires: baobab-locales = %{version}-%{release}
Requires: baobab-man = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : vala
BuildRequires : vala-dev

%description
# Baobab
Baobab is the GNOME [Disk Usage Analyzer](https://wiki.gnome.org/Apps/DiskUsageAnalyzer).

%package bin
Summary: bin components for the baobab package.
Group: Binaries
Requires: baobab-data = %{version}-%{release}
Requires: baobab-license = %{version}-%{release}

%description bin
bin components for the baobab package.


%package data
Summary: data components for the baobab package.
Group: Data

%description data
data components for the baobab package.


%package doc
Summary: doc components for the baobab package.
Group: Documentation
Requires: baobab-man = %{version}-%{release}

%description doc
doc components for the baobab package.


%package license
Summary: license components for the baobab package.
Group: Default

%description license
license components for the baobab package.


%package locales
Summary: locales components for the baobab package.
Group: Default

%description locales
locales components for the baobab package.


%package man
Summary: man components for the baobab package.
Group: Default

%description man
man components for the baobab package.


%prep
%setup -q -n baobab-40.0
cd %{_builddir}/baobab-40.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619050503
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/baobab
cp %{_builddir}/baobab-40.0/COPYING %{buildroot}/usr/share/package-licenses/baobab/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/baobab-40.0/COPYING.docs %{buildroot}/usr/share/package-licenses/baobab/4f485ab7059ac53d9e3818278ad82217ce976a36
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang baobab

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/baobab

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.baobab.desktop
/usr/share/dbus-1/services/org.gnome.baobab.service
/usr/share/glib-2.0/schemas/org.gnome.baobab.gschema.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.baobab.Devel.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.baobab.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.baobab-symbolic.svg
/usr/share/metainfo/org.gnome.baobab.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/baobab/index.page
/usr/share/help/C/baobab/introduction.page
/usr/share/help/C/baobab/legal.xml
/usr/share/help/C/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/C/baobab/pref-view-chart.page
/usr/share/help/C/baobab/problem-permissions.page
/usr/share/help/C/baobab/problem-slow-scan.page
/usr/share/help/C/baobab/question-open-folder.page
/usr/share/help/C/baobab/question-trash.page
/usr/share/help/C/baobab/scan-file-system.page
/usr/share/help/C/baobab/scan-folder.page
/usr/share/help/C/baobab/scan-home.page
/usr/share/help/C/baobab/scan-remote.page
/usr/share/help/ca/baobab/index.page
/usr/share/help/ca/baobab/introduction.page
/usr/share/help/ca/baobab/legal.xml
/usr/share/help/ca/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/ca/baobab/pref-view-chart.page
/usr/share/help/ca/baobab/problem-permissions.page
/usr/share/help/ca/baobab/problem-slow-scan.page
/usr/share/help/ca/baobab/question-open-folder.page
/usr/share/help/ca/baobab/question-trash.page
/usr/share/help/ca/baobab/scan-file-system.page
/usr/share/help/ca/baobab/scan-folder.page
/usr/share/help/ca/baobab/scan-home.page
/usr/share/help/ca/baobab/scan-remote.page
/usr/share/help/cs/baobab/index.page
/usr/share/help/cs/baobab/introduction.page
/usr/share/help/cs/baobab/legal.xml
/usr/share/help/cs/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/cs/baobab/pref-view-chart.page
/usr/share/help/cs/baobab/problem-permissions.page
/usr/share/help/cs/baobab/problem-slow-scan.page
/usr/share/help/cs/baobab/question-open-folder.page
/usr/share/help/cs/baobab/question-trash.page
/usr/share/help/cs/baobab/scan-file-system.page
/usr/share/help/cs/baobab/scan-folder.page
/usr/share/help/cs/baobab/scan-home.page
/usr/share/help/cs/baobab/scan-remote.page
/usr/share/help/da/baobab/index.page
/usr/share/help/da/baobab/introduction.page
/usr/share/help/da/baobab/legal.xml
/usr/share/help/da/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/da/baobab/pref-view-chart.page
/usr/share/help/da/baobab/problem-permissions.page
/usr/share/help/da/baobab/problem-slow-scan.page
/usr/share/help/da/baobab/question-open-folder.page
/usr/share/help/da/baobab/question-trash.page
/usr/share/help/da/baobab/scan-file-system.page
/usr/share/help/da/baobab/scan-folder.page
/usr/share/help/da/baobab/scan-home.page
/usr/share/help/da/baobab/scan-remote.page
/usr/share/help/de/baobab/index.page
/usr/share/help/de/baobab/introduction.page
/usr/share/help/de/baobab/legal.xml
/usr/share/help/de/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/de/baobab/pref-view-chart.page
/usr/share/help/de/baobab/problem-permissions.page
/usr/share/help/de/baobab/problem-slow-scan.page
/usr/share/help/de/baobab/question-open-folder.page
/usr/share/help/de/baobab/question-trash.page
/usr/share/help/de/baobab/scan-file-system.page
/usr/share/help/de/baobab/scan-folder.page
/usr/share/help/de/baobab/scan-home.page
/usr/share/help/de/baobab/scan-remote.page
/usr/share/help/el/baobab/index.page
/usr/share/help/el/baobab/introduction.page
/usr/share/help/el/baobab/legal.xml
/usr/share/help/el/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/el/baobab/pref-view-chart.page
/usr/share/help/el/baobab/problem-permissions.page
/usr/share/help/el/baobab/problem-slow-scan.page
/usr/share/help/el/baobab/question-open-folder.page
/usr/share/help/el/baobab/question-trash.page
/usr/share/help/el/baobab/scan-file-system.page
/usr/share/help/el/baobab/scan-folder.page
/usr/share/help/el/baobab/scan-home.page
/usr/share/help/el/baobab/scan-remote.page
/usr/share/help/es/baobab/index.page
/usr/share/help/es/baobab/introduction.page
/usr/share/help/es/baobab/legal.xml
/usr/share/help/es/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/es/baobab/pref-view-chart.page
/usr/share/help/es/baobab/problem-permissions.page
/usr/share/help/es/baobab/problem-slow-scan.page
/usr/share/help/es/baobab/question-open-folder.page
/usr/share/help/es/baobab/question-trash.page
/usr/share/help/es/baobab/scan-file-system.page
/usr/share/help/es/baobab/scan-folder.page
/usr/share/help/es/baobab/scan-home.page
/usr/share/help/es/baobab/scan-remote.page
/usr/share/help/fi/baobab/index.page
/usr/share/help/fi/baobab/introduction.page
/usr/share/help/fi/baobab/legal.xml
/usr/share/help/fi/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/fi/baobab/pref-view-chart.page
/usr/share/help/fi/baobab/problem-permissions.page
/usr/share/help/fi/baobab/problem-slow-scan.page
/usr/share/help/fi/baobab/question-open-folder.page
/usr/share/help/fi/baobab/question-trash.page
/usr/share/help/fi/baobab/scan-file-system.page
/usr/share/help/fi/baobab/scan-folder.page
/usr/share/help/fi/baobab/scan-home.page
/usr/share/help/fi/baobab/scan-remote.page
/usr/share/help/fr/baobab/index.page
/usr/share/help/fr/baobab/introduction.page
/usr/share/help/fr/baobab/legal.xml
/usr/share/help/fr/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/fr/baobab/pref-view-chart.page
/usr/share/help/fr/baobab/problem-permissions.page
/usr/share/help/fr/baobab/problem-slow-scan.page
/usr/share/help/fr/baobab/question-open-folder.page
/usr/share/help/fr/baobab/question-trash.page
/usr/share/help/fr/baobab/scan-file-system.page
/usr/share/help/fr/baobab/scan-folder.page
/usr/share/help/fr/baobab/scan-home.page
/usr/share/help/fr/baobab/scan-remote.page
/usr/share/help/gl/baobab/index.page
/usr/share/help/gl/baobab/introduction.page
/usr/share/help/gl/baobab/legal.xml
/usr/share/help/gl/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/gl/baobab/pref-view-chart.page
/usr/share/help/gl/baobab/problem-permissions.page
/usr/share/help/gl/baobab/problem-slow-scan.page
/usr/share/help/gl/baobab/question-open-folder.page
/usr/share/help/gl/baobab/question-trash.page
/usr/share/help/gl/baobab/scan-file-system.page
/usr/share/help/gl/baobab/scan-folder.page
/usr/share/help/gl/baobab/scan-home.page
/usr/share/help/gl/baobab/scan-remote.page
/usr/share/help/hr/baobab/index.page
/usr/share/help/hr/baobab/introduction.page
/usr/share/help/hr/baobab/legal.xml
/usr/share/help/hr/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/hr/baobab/pref-view-chart.page
/usr/share/help/hr/baobab/problem-permissions.page
/usr/share/help/hr/baobab/problem-slow-scan.page
/usr/share/help/hr/baobab/question-open-folder.page
/usr/share/help/hr/baobab/question-trash.page
/usr/share/help/hr/baobab/scan-file-system.page
/usr/share/help/hr/baobab/scan-folder.page
/usr/share/help/hr/baobab/scan-home.page
/usr/share/help/hr/baobab/scan-remote.page
/usr/share/help/hu/baobab/index.page
/usr/share/help/hu/baobab/introduction.page
/usr/share/help/hu/baobab/legal.xml
/usr/share/help/hu/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/hu/baobab/pref-view-chart.page
/usr/share/help/hu/baobab/problem-permissions.page
/usr/share/help/hu/baobab/problem-slow-scan.page
/usr/share/help/hu/baobab/question-open-folder.page
/usr/share/help/hu/baobab/question-trash.page
/usr/share/help/hu/baobab/scan-file-system.page
/usr/share/help/hu/baobab/scan-folder.page
/usr/share/help/hu/baobab/scan-home.page
/usr/share/help/hu/baobab/scan-remote.page
/usr/share/help/id/baobab/index.page
/usr/share/help/id/baobab/introduction.page
/usr/share/help/id/baobab/legal.xml
/usr/share/help/id/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/id/baobab/pref-view-chart.page
/usr/share/help/id/baobab/problem-permissions.page
/usr/share/help/id/baobab/problem-slow-scan.page
/usr/share/help/id/baobab/question-open-folder.page
/usr/share/help/id/baobab/question-trash.page
/usr/share/help/id/baobab/scan-file-system.page
/usr/share/help/id/baobab/scan-folder.page
/usr/share/help/id/baobab/scan-home.page
/usr/share/help/id/baobab/scan-remote.page
/usr/share/help/it/baobab/index.page
/usr/share/help/it/baobab/introduction.page
/usr/share/help/it/baobab/legal.xml
/usr/share/help/it/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/it/baobab/pref-view-chart.page
/usr/share/help/it/baobab/problem-permissions.page
/usr/share/help/it/baobab/problem-slow-scan.page
/usr/share/help/it/baobab/question-open-folder.page
/usr/share/help/it/baobab/question-trash.page
/usr/share/help/it/baobab/scan-file-system.page
/usr/share/help/it/baobab/scan-folder.page
/usr/share/help/it/baobab/scan-home.page
/usr/share/help/it/baobab/scan-remote.page
/usr/share/help/ko/baobab/index.page
/usr/share/help/ko/baobab/introduction.page
/usr/share/help/ko/baobab/legal.xml
/usr/share/help/ko/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/ko/baobab/pref-view-chart.page
/usr/share/help/ko/baobab/problem-permissions.page
/usr/share/help/ko/baobab/problem-slow-scan.page
/usr/share/help/ko/baobab/question-open-folder.page
/usr/share/help/ko/baobab/question-trash.page
/usr/share/help/ko/baobab/scan-file-system.page
/usr/share/help/ko/baobab/scan-folder.page
/usr/share/help/ko/baobab/scan-home.page
/usr/share/help/ko/baobab/scan-remote.page
/usr/share/help/pl/baobab/index.page
/usr/share/help/pl/baobab/introduction.page
/usr/share/help/pl/baobab/legal.xml
/usr/share/help/pl/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/pl/baobab/pref-view-chart.page
/usr/share/help/pl/baobab/problem-permissions.page
/usr/share/help/pl/baobab/problem-slow-scan.page
/usr/share/help/pl/baobab/question-open-folder.page
/usr/share/help/pl/baobab/question-trash.page
/usr/share/help/pl/baobab/scan-file-system.page
/usr/share/help/pl/baobab/scan-folder.page
/usr/share/help/pl/baobab/scan-home.page
/usr/share/help/pl/baobab/scan-remote.page
/usr/share/help/pt/baobab/index.page
/usr/share/help/pt/baobab/introduction.page
/usr/share/help/pt/baobab/legal.xml
/usr/share/help/pt/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/pt/baobab/pref-view-chart.page
/usr/share/help/pt/baobab/problem-permissions.page
/usr/share/help/pt/baobab/problem-slow-scan.page
/usr/share/help/pt/baobab/question-open-folder.page
/usr/share/help/pt/baobab/question-trash.page
/usr/share/help/pt/baobab/scan-file-system.page
/usr/share/help/pt/baobab/scan-folder.page
/usr/share/help/pt/baobab/scan-home.page
/usr/share/help/pt/baobab/scan-remote.page
/usr/share/help/pt_BR/baobab/index.page
/usr/share/help/pt_BR/baobab/introduction.page
/usr/share/help/pt_BR/baobab/legal.xml
/usr/share/help/pt_BR/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/pt_BR/baobab/pref-view-chart.page
/usr/share/help/pt_BR/baobab/problem-permissions.page
/usr/share/help/pt_BR/baobab/problem-slow-scan.page
/usr/share/help/pt_BR/baobab/question-open-folder.page
/usr/share/help/pt_BR/baobab/question-trash.page
/usr/share/help/pt_BR/baobab/scan-file-system.page
/usr/share/help/pt_BR/baobab/scan-folder.page
/usr/share/help/pt_BR/baobab/scan-home.page
/usr/share/help/pt_BR/baobab/scan-remote.page
/usr/share/help/ru/baobab/index.page
/usr/share/help/ru/baobab/introduction.page
/usr/share/help/ru/baobab/legal.xml
/usr/share/help/ru/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/ru/baobab/pref-view-chart.page
/usr/share/help/ru/baobab/problem-permissions.page
/usr/share/help/ru/baobab/problem-slow-scan.page
/usr/share/help/ru/baobab/question-open-folder.page
/usr/share/help/ru/baobab/question-trash.page
/usr/share/help/ru/baobab/scan-file-system.page
/usr/share/help/ru/baobab/scan-folder.page
/usr/share/help/ru/baobab/scan-home.page
/usr/share/help/ru/baobab/scan-remote.page
/usr/share/help/sl/baobab/index.page
/usr/share/help/sl/baobab/introduction.page
/usr/share/help/sl/baobab/legal.xml
/usr/share/help/sl/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/sl/baobab/pref-view-chart.page
/usr/share/help/sl/baobab/problem-permissions.page
/usr/share/help/sl/baobab/problem-slow-scan.page
/usr/share/help/sl/baobab/question-open-folder.page
/usr/share/help/sl/baobab/question-trash.page
/usr/share/help/sl/baobab/scan-file-system.page
/usr/share/help/sl/baobab/scan-folder.page
/usr/share/help/sl/baobab/scan-home.page
/usr/share/help/sl/baobab/scan-remote.page
/usr/share/help/sv/baobab/index.page
/usr/share/help/sv/baobab/introduction.page
/usr/share/help/sv/baobab/legal.xml
/usr/share/help/sv/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/sv/baobab/pref-view-chart.page
/usr/share/help/sv/baobab/problem-permissions.page
/usr/share/help/sv/baobab/problem-slow-scan.page
/usr/share/help/sv/baobab/question-open-folder.page
/usr/share/help/sv/baobab/question-trash.page
/usr/share/help/sv/baobab/scan-file-system.page
/usr/share/help/sv/baobab/scan-folder.page
/usr/share/help/sv/baobab/scan-home.page
/usr/share/help/sv/baobab/scan-remote.page
/usr/share/help/uk/baobab/index.page
/usr/share/help/uk/baobab/introduction.page
/usr/share/help/uk/baobab/legal.xml
/usr/share/help/uk/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/uk/baobab/pref-view-chart.page
/usr/share/help/uk/baobab/problem-permissions.page
/usr/share/help/uk/baobab/problem-slow-scan.page
/usr/share/help/uk/baobab/question-open-folder.page
/usr/share/help/uk/baobab/question-trash.page
/usr/share/help/uk/baobab/scan-file-system.page
/usr/share/help/uk/baobab/scan-folder.page
/usr/share/help/uk/baobab/scan-home.page
/usr/share/help/uk/baobab/scan-remote.page
/usr/share/help/zh_CN/baobab/index.page
/usr/share/help/zh_CN/baobab/introduction.page
/usr/share/help/zh_CN/baobab/legal.xml
/usr/share/help/zh_CN/baobab/media/hicolor_apps_48x48_baobab.png
/usr/share/help/zh_CN/baobab/pref-view-chart.page
/usr/share/help/zh_CN/baobab/problem-permissions.page
/usr/share/help/zh_CN/baobab/problem-slow-scan.page
/usr/share/help/zh_CN/baobab/question-open-folder.page
/usr/share/help/zh_CN/baobab/question-trash.page
/usr/share/help/zh_CN/baobab/scan-file-system.page
/usr/share/help/zh_CN/baobab/scan-folder.page
/usr/share/help/zh_CN/baobab/scan-home.page
/usr/share/help/zh_CN/baobab/scan-remote.page

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/baobab/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/baobab/4f485ab7059ac53d9e3818278ad82217ce976a36

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/baobab.1

%files locales -f baobab.lang
%defattr(-,root,root,-)

