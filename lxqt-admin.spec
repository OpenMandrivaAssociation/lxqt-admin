%define git 0
Name: lxqt-admin
Version: 0.17.0
%if %git
Release: 1.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: https://github.com/lxqt/lxqt-admin/releases/download/%{version}/lxqt-admin-%{version}.tar.xz
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
BuildRequires: cmake(PolkitQt5-1)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(liboobs-1)
BuildRequires: lxqt-build-tools git-core
Requires: system-tools-backends2

%description
Admin tools for the LXQt desktop.

%prep
%if %git
%autosetup -p1 -n %{name}-%{git}
%else
%autosetup -p1
%endif

%cmake_qt5 \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	-G Ninja

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
%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%{_bindir}/lxqt-admin-time
%{_bindir}/lxqt-admin-time-helper
%{_bindir}/lxqt-admin-user
%{_bindir}/lxqt-admin-user-helper
%{_datadir}/applications/lxqt-admin-time.desktop
%{_datadir}/applications/lxqt-admin-user.desktop
%{_datadir}/polkit-1/actions/org.lxqt.lxqt-admin-time.policy
%{_datadir}/polkit-1/actions/org.lxqt.lxqt-admin-user.policy
%lang(arn) %{_datadir}/lxqt/translations/lxqt-admin-time/lxqt-admin-time_arn.qm
%lang(ast) %{_datadir}/lxqt/translations/lxqt-admin-time/lxqt-admin-time_ast.qm
%lang(arn) %{_datadir}/lxqt/translations/lxqt-admin-user/lxqt-admin-user_arn.qm
%lang(ast) %{_datadir}/lxqt/translations/lxqt-admin-user/lxqt-admin-user_ast.qm
