%define git 0
Name: lxqt-admin
Version: 0.9.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 2
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Summary: Admin tools for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(liboobs-1)
BuildRequires: qt5-devel
BuildRequires: desktop-file-utils
Requires: system-tools-backends2

%description
Admin tools for the LXQt desktop

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%cmake -DUSE_QT5:BOOL=ON

%build
%make -C build

%install
%makeinstall_std -C build

for name in admin-time admin-user; do
    desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
	--remove-only-show-in=LXQt --add-only-show-in=X-LXQt %{buildroot}%{_datadir}/applications/lxqt-${name}.desktop
done

%find_lang %{name}-time --with-qt
%find_lang %{name}-user --with-qt

%files -f %{name}-time.lang -f %{name}-user.lang
%{_bindir}/lxqt-admin-time
%{_bindir}/lxqt-admin-user
%{_datadir}/applications/lxqt-admin-time.desktop
%{_datadir}/applications/lxqt-admin-user.desktop
