Name:           darwinx-libgcrypt
Version:        1.6.1
Release:        1%{?dist}
Summary:        Libgcrypt is a general purpose cryptographic library based on the code from GnuPG

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.gnu.org/software/libgcrypt/
Source0:        libgcrypt-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  darwinx-filesystem >= 2
BuildRequires:  darwinx-gcc
BuildRequires:  darwinx-gettext


%description
Libgcrypt is a general purpose cryptographic library based on the code from GnuPG

%package static
Summary:        Libgcrypt is a general purpose cryptographic library based on the code from GnuPG
Requires:       %{name} = %{version}-%{release}
Group:          Development/Libraries

%description static
Libgcrypt is a general purpose cryptographic library based on the code from GnuPG

%prep
%setup -q -n libgcrypt-%{version}


%build
%{_darwinx_configure} \
	--enable-static \
	--disable-asm
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{_darwinx_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_darwinx_bindir}/dumpsexp
%{_darwinx_bindir}/hmac256
%{_darwinx_bindir}/libgcrypt-config
%{_darwinx_bindir}/mpicalc
%{_darwinx_libdir}/libgcrypt.dylib
%{_darwinx_libdir}/libgcrypt.la
%{_darwinx_libdir}/libgcrypt.*.dylib
%{_darwinx_includedir}/gcrypt.h

%files static
%defattr(-,root,root)
%{_darwinx_libdir}/libgcrypt.a

%changelog
* Thu Feb 27 2014 Mikkel Kruse Johnsen <mikkel@structura-it.dk> - 3.0.13-1
- Initial RPM release
