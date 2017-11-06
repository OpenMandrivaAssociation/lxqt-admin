%define git 0
Name: lxqt-admin
Version: 0.12.0
%if %git
Release: 1.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
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

%cmake_qt5 -G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build

%find_lang %{name}-time --with-qt
%find_lang %{name}-user --with-qt

%files -f %{name}-time.lang -f %{name}-user.lang
%{_bindir}/lxqt-admin-time
%{_bindir}/lxqt-admin-user
%{_bindir}/lxqt-admin-user-helper
%{_datadir}/applications/lxqt-admin-time.desktop
%{_datadir}/applications/lxqt-admin-user.desktop
%{_datadir}/polkit-1/actions/org.lxqt.lxqt-admin-user.policy
%{_datadir}/lxqt/translations/lxqt-admin-time/lxqt-admin-time_*.qm
