%define git 0
Name: lxqt-admin
Version: 0.10.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 7
Source0: https://github.com/lxde/%{name}/archive/%{name}-%{version}.tar.xz
%endif
Summary: Admin tools for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: ninja
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(liboobs-1)
Requires: system-tools-backends2

%description
Admin tools for the LXQt desktop.

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%cmake -G Ninja

%build
# To make grep happy about UTF-8 translations in desktop files
export LC_ALL=en_US.utf-8
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}-time --with-qt
%find_lang %{name}-user --with-qt

%files -f %{name}-time.lang -f %{name}-user.lang
%{_bindir}/lxqt-admin-time
%{_bindir}/lxqt-admin-user
%{_datadir}/applications/lxqt-admin-time.desktop
%{_datadir}/applications/lxqt-admin-user.desktop
%{_datadir}/lxqt/translations/lxqt-admin-time/lxqt-admin-time_*.qm
