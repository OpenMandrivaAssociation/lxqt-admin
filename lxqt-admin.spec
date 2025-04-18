Name: lxqt-admin
Version: 2.2.0
Release: %{?snapshot:1.%{snapshot}.}1
Source0: https://github.com/lxqt/lxqt-admin/releases/download/%{version}/lxqt-admin-%{version}.tar.xz
Summary: Admin tools for the LXQt desktop
URL: https://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(PolkitQt6-1)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(liboobs-1)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: lxqt-build-tools git-core
Requires: system-tools-backends2

%description
Admin tools for the LXQt desktop.

%prep
%autosetup -p1
%cmake \
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
%{_bindir}/lxqt-admin-user
%{_bindir}/lxqt-admin-user-helper
%{_datadir}/applications/lxqt-admin-time.desktop
%{_datadir}/applications/lxqt-admin-user.desktop
%{_datadir}/polkit-1/actions/org.lxqt.lxqt-admin-user.policy
