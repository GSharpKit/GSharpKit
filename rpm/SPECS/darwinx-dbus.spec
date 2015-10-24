Name:           darwinx-dbus
Version:        1.8.16
Release:        2%{?dist}
Summary:        D-Bus Message Bus System

License:        Dual GPLv2 or AFLv2.1
Group:          Development/Libraries
URL:            http://dbus.freedesktop.org/
Source0:        http://dbus.freedesktop.org/releases/dbus/dbus-%{version}.tar.gz
Source1:	dbus-install.sh

Patch0:		dbus-1.6.8-launchctl.patch
Patch1:		darwinx-dbus-multi-arch.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 13

%description
D-Bus is a message bus system, a simple way for applications to talk to
one another. D-Bus supplies both a system daemon and a
per-user-login-session daemon. Also, the message bus is built on top of
a general one-to-one message passing framework, which can be used by
any two apps to communicate directly (without going through the message
bus daemon).

%prep
%setup -q -n dbus-%{version}
%patch0 -p1 -b .launchctl
%patch1 -p1

%build
libtoolize --force --copy --install
autoreconf -f -i
echo "lt_cv_deplibs_check_method='pass_all'" >>%{_darwinx_cache}
%{_darwinx_configure} \
	--enable-maintainer-mode \
	--disable-static \
	--enable-verbose-mode \
	--disable-tests \
	--enable-checks \
	--enable-asserts \
	--enable-launchd
make %{?_smp_mflags} || make


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

install -m 775 %{SOURCE1} $RPM_BUILD_ROOT%{_darwinx_bindir}/

rm -rf $RPM_BUILD_ROOT%{_darwinx_sysconfdir}/rc.d
rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}/doc

mv $RPM_BUILD_ROOT/Library $RPM_BUILD_ROOT%{_darwinx_prefix}

sed -i '' 's!\/usr\/darwinx!!' $RPM_BUILD_ROOT%{_darwinx_prefix}/Library/LaunchAgents/org.freedesktop.dbus-session.plist
sed -i '' 's!\/usr\/bin!\/usr\/local\/bin!' $RPM_BUILD_ROOT%{_darwinx_prefix}/Library/LaunchAgents/org.freedesktop.dbus-session.plist
sed -i '' 's!--session!--config-file=\/etc\/dbus-1\/session.conf!' $RPM_BUILD_ROOT%{_darwinx_prefix}/Library/LaunchAgents/org.freedesktop.dbus-session.plist
sed -i '' 's!false !true!' $RPM_BUILD_ROOT%{_darwinx_prefix}/Library/LaunchAgents/org.freedesktop.dbus-session.plist

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_darwinx_libdir}/libdbus-1.*.dylib
%{_darwinx_bindir}/dbus-run-session
%{_darwinx_bindir}/dbus-install.sh
%{_darwinx_bindir}/dbus-monitor
%{_darwinx_bindir}/dbus-launch
%{_darwinx_bindir}/dbus-send
%{_darwinx_bindir}/dbus-daemon
%{_darwinx_bindir}/dbus-cleanup-sockets
%{_darwinx_bindir}/dbus-uuidgen
%{_darwinx_libexecdir}/dbus-daemon-launch-helper
%{_darwinx_prefix}/Library/LaunchAgents/org.freedesktop.dbus-session.plist
%{_darwinx_sysconfdir}/dbus-1/session.conf
%dir %{_darwinx_sysconfdir}/dbus-1/session.d
%{_darwinx_sysconfdir}/dbus-1/system.conf
%dir %{_darwinx_sysconfdir}/dbus-1/system.d
%dir %{_darwinx_datadir}/dbus-1/services
%dir %{_darwinx_datadir}/dbus-1/system-services
#%dir %{_darwinx_localstatedir}/lib/dbus
%dir %{_darwinx_localstatedir}/run/dbus

%{_darwinx_libdir}/libdbus-1.dylib
%{_darwinx_includedir}/dbus-1.0/dbus/*.h
%{_darwinx_libdir}/libdbus-1.la
%{_darwinx_libdir}/pkgconfig/dbus-1.pc
%{_darwinx_libdir}/dbus-1.0/include/dbus/dbus-arch-deps.h

%changelog
