Name:           darwinx-libsecret
Version:        0.16
Release:        1%{?dist}
Summary:        Library for storing and retrieving passwords and other secrets
License:        LGPLv2+
Group:          Development/Libraries
URL:            https://live.gnome.org/Libsecret
Source0:        libsecret-%{version}.tar.xz
Patch0:		libsecret-0.16-disable-docs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 12
BuildRequires:  darwinx-gcc

%description
libsecret is a library for storing and retrieving passwords and other secrets.
It communicates with the "Secret Service" using DBus. gnome-keyring and
KSecretService are both implementations of a Secret Service.

%prep
%setup -q -n libsecret-%{version}
%patch0 -p1

%build
%{_darwinx_configure} \
	--disable-static \
	--disable-gtk-doc-html \
	--disable-man-pages

%{_darwinx_make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%{_darwinx_bindir}/secret-tool
%{_darwinx_includedir}/libsecret-1
%{_darwinx_libdir}/libsecret-1.*.dylib
%{_darwinx_libdir}/libsecret-1.dylib
%{_darwinx_libdir}/libsecret-1.la
%{_darwinx_libdir}/pkgconfig/libsecret-1.pc
%{_darwinx_libdir}/pkgconfig/libsecret-unstable.pc

%changelog
* Thu May  9 2013 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 5.1.1-1
- Initial RPM release.
