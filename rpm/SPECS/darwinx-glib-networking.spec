Name:           darwinx-glib-networking
Version:        2.54.1
Release:        1%{?dist}
Summary:        Networking support for GLib 

License:        GPLv3+ and LGPLv2+
Group:          Development/Libraries
URL:            http://ftp.gnome.org/pub/GNOME/sources/glib-networking/2.48/
Source0:        glib-networking-%{version}.tar.xz
Patch0:		glib-networking-2.38.2-error-format.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem-base >= 18
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-libgpg-error
BuildRequires:  darwinx-libgcrypt
BuildRequires:  darwinx-gnutls

BuildRequires:  pkgconfig

Requires:  	darwinx-filesystem >= 18

%description
This package contains modules that extend the networking support in
GIO. In particular, it contains libproxy- and GSettings-based
GProxyResolver implementations and a gnutls-based GTlsConnection
implementation.

%prep
%setup -q -n glib-networking-%{version}
#%patch0 -p1

%build
%{_darwinx_configure} \
	--disable-static \
	--disable-nls \
	--without-ca-certificates \
	--disable-gtk-doc

%{_darwinx_make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%{_darwinx_libdir}/gio/modules/libgiognutls.so
%{_darwinx_libdir}/gio/modules/libgiognutls.la

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.36.1-1
- Initial RPM release.

