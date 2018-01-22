#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : baobab
Version  : 3.26.1
Release  : 7
URL      : https://download.gnome.org/sources/baobab/3.26/baobab-3.26.1.tar.xz
Source0  : https://download.gnome.org/sources/baobab/3.26/baobab-3.26.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0
Requires: baobab-bin
Requires: baobab-data
Requires: baobab-doc
Requires: baobab-locales
BuildRequires : gettext
BuildRequires : itstool
BuildRequires : libxml2-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)

%description
What is Baobab
==============
Baobab is a simple application which can scan either specific folders
(local or remote) or volumes and give a graphical representation
including each directory size or percentage in the branch. It also
auto-detects any mounted/unmounted device.

%package bin
Summary: bin components for the baobab package.
Group: Binaries
Requires: baobab-data

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

%description doc
doc components for the baobab package.


%package locales
Summary: locales components for the baobab package.
Group: Default

%description locales
locales components for the baobab package.


%prep
%setup -q -n baobab-3.26.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1516655515
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1516655515
rm -rf %{buildroot}
%make_install
%find_lang baobab

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/baobab

%files data
%defattr(-,root,root,-)
/usr/share/appdata/org.gnome.baobab.appdata.xml
/usr/share/applications/org.gnome.baobab.desktop
/usr/share/dbus-1/services/org.gnome.baobab.service
/usr/share/glib-2.0/schemas/org.gnome.baobab.gschema.xml
/usr/share/icons/hicolor/16x16/apps/baobab.png
/usr/share/icons/hicolor/22x22/apps/baobab.png
/usr/share/icons/hicolor/24x24/apps/baobab.png
/usr/share/icons/hicolor/256x256/apps/baobab.png
/usr/share/icons/hicolor/32x32/apps/baobab.png
/usr/share/icons/hicolor/48x48/apps/baobab.png
/usr/share/icons/hicolor/scalable/apps/baobab-symbolic.svg

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
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

%files locales -f baobab.lang
%defattr(-,root,root,-)

