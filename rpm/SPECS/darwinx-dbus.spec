Name:           darwinx-dbus
Version:        1.14.10
Release:        1%{?dist}
Summary:        D-Bus Message Bus System

License:        Dual GPLv2 or AFLv2.1
Group:          Development/Libraries
URL:            http://dbus.freedesktop.org/
Source0:        http://dbus.freedesktop.org/releases/dbus/dbus-%{version}.tar.xz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  darwinx-filesystem-base >= 106

Requires:  	darwinx-filesystem >= 106

%description
D-Bus is a message bus system, a simple way for applications to talk to
one another. D-Bus supplies both a system daemon and a
per-user-login-session daemon. Also, the message bus is built on top of
a general one-to-one message passing framework, which can be used by
any two apps to communicate directly (without going through the message
bus daemon).

%prep
%setup -q -n dbus-%{version}

%build
%{_darwinx_configure} \
       --enable-maintainer-mode \
       --disable-static \
       --enable-verbose-mode \
       --disable-tests \
       --enable-checks \
       --enable-asserts \
       --enable-launchd \
       --with-dbus-daemondir=/Library/Frameworks/GSharpKit/bin
make %{?_smp_mflags} || make

# WARNING: dbus-daemon is build with @rpath and not full path
#darwinx_meson \
#	-Dlaunchd=enabled \
#	-Dxml_docs=disabled \
#	-Ddoxygen_docs=disabled \
#	-Dducktype_docs=disabled \
#	-Dqt_help=disabled \
#	-Dselinux=disabled \
#	-Dapparmor=disabled \
#	-Dinotify=disabled \
#	-Depoll=disabled \
#	-Dsystemd=disabled \
#	-Dlibaudit=disabled \
#	-Dx11_autolaunch=disabled
#
#darwinx_meson_build
#
#install
#darwinx_meson_install

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_sysconfdir}/rc.d
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/xml
rm -rf $RPM_BUILD_ROOT%{_darwinx_libdir}/cmake

sed -i '' 's!unix:tmpdir=\/tmp!launchd:env=DBUS_LAUNCHD_SESSION_BUS_SOCKET!' $RPM_BUILD_ROOT%{_darwinx_prefix}/share/dbus-1/session.conf 
sed -i '' 's!\/usr\/local!\/usr!' $RPM_BUILD_ROOT/Library/LaunchAgents/org.freedesktop.dbus-session.plist
sed -i '' 's!--session!--config-file=\/Library\/Frameworks\/GSharpKit\/share\/dbus-1\/session.conf!' $RPM_BUILD_ROOT/Library/LaunchAgents/org.freedesktop.dbus-session.plist
sed -i '' 's!false !true!' $RPM_BUILD_ROOT/Library/LaunchAgents/org.freedesktop.dbus-session.plist

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,wheel)
%{_darwinx_libdir}/libdbus-1.*.dylib
%{_darwinx_libdir}/libdbus-1.dylib
%{_darwinx_bindir}/dbus-run-session
%{_darwinx_bindir}/dbus-monitor
%{_darwinx_bindir}/dbus-launch
%{_darwinx_bindir}/dbus-send
%{_darwinx_bindir}/dbus-daemon
%{_darwinx_bindir}/dbus-cleanup-sockets
%{_darwinx_bindir}/dbus-uuidgen
%{_darwinx_bindir}/dbus-test-tool
%{_darwinx_bindir}/dbus-update-activation-environment
%{_darwinx_libexecdir}/dbus-daemon-launch-helper
/Library/LaunchAgents/org.freedesktop.dbus-session.plist
%{_darwinx_sysconfdir}/dbus-1/session.conf
%{_darwinx_datadir}/dbus-1/session.conf
%dir %{_darwinx_datadir}/dbus-1/session.d
%{_darwinx_sysconfdir}/dbus-1/system.conf
%{_darwinx_datadir}/dbus-1/system.conf
%dir %{_darwinx_datadir}/dbus-1/system.d
%dir %{_darwinx_datadir}/dbus-1/services
%dir %{_darwinx_datadir}/dbus-1/system-services
%dir %{_darwinx_localstatedir}/lib/dbus
%dir %{_darwinx_localstatedir}/run/dbus
%{_darwinx_includedir}/dbus-1.0/dbus/*.h
%{_darwinx_libdir}/pkgconfig/dbus-1.pc
%{_darwinx_libdir}/dbus-1.0/include/dbus/dbus-arch-deps.h

%changelog
