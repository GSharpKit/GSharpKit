Name:           darwinx-dbus-glib
Version:        0.108
Release:        1%{?dist}
Summary:        D-Bus Message Bus System

License:        Dual GPLv2 or AFLv2.1
Group:          Development/Libraries
URL:            http://dbus.freedesktop.org/
Source:         http://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-glib2
BuildRequires:  darwinx-dbus

Requires:  	darwinx-filesystem >= 18

%description
D-Bus is a message bus system, a simple way for applications to talk to
one another. D-Bus supplies both a system daemon and a
per-user-login-session daemon. Also, the message bus is built on top of
a general one-to-one message passing framework, which can be used by
any two apps to communicate directly (without going through the message
bus daemon).


%prep
%setup -q -n dbus-glib-%{version}

%build
export ac_cv_have_abstract_sockets="no"
export lt_cv_deplibs_check_method="pass_all"
%{_darwinx_configure} \
	--enable-shared \
	--disable-static
make %{?_smp_mflags} || make


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT program_transform_name=""


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_darwinx_libdir}/libdbus-glib-1.*.dylib
%{_darwinx_libexecdir}/dbus-bash-completion-helper
%{_darwinx_sysconfdir}/bash_completion.d/dbus-bash-completion.sh
%{_darwinx_includedir}/dbus-1.0/dbus/*.h
%{_darwinx_libdir}/libdbus-glib-1.la
%{_darwinx_libdir}/libdbus-glib-1.dylib
%{_darwinx_libdir}/pkgconfig/dbus-glib-1.pc
%{_darwinx_datadir}/gtk-doc/html/dbus-glib
%{_darwinx_bindir}/dbus-binding-tool
%{_darwinx_mandir}/man1/dbus-binding-tool.1*

%changelog
