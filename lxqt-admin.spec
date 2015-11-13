%define git 0
Name: lxqt-admin
Version: 0.10.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: https://github.com/lxde/%{name}/archive/%{version}.tar.gz
%endif
Summary: Admin tools for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: qmake5
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
%cmake

%build
%make -C build

%install
%makeinstall_std -C build


%find_lang %{name}-time --with-qt
%find_lang %{name}-user --with-qt

%files -f %{name}-time.lang -f %{name}-user.lang
%{_bindir}/lxqt-admin-time
%{_bindir}/lxqt-admin-user
%{_datadir}/applications/lxqt-admin-time.desktop
%{_datadir}/applications/lxqt-admin-user.desktop
%{_datadir}/lxqt/translations/lxqt-admin-time/lxqt-admin-time_*.qm
