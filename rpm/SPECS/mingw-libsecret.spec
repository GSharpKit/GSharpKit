%?mingw_package_header

Name:           mingw-libsecret
Version:        0.18.5
Release:        1%{?dist}
Summary:        GObject based library for accessing the Secret Service API.

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://github.com/GNOME/libsecret/
Source0:        https://github.com/GNOME/libsecret/archive/libsecret-%{version}.tar.gz
Patch0:		mingw-libsecret.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

%description
GObject based library for accessing the Secret Service API.

%package -n mingw32-libsecret
Summary:        MinGW Windows GTK+ library
Requires:       pkgconfig

%description -n mingw32-libsecret
GObject based library for accessing the Secret Service API.

%package -n mingw64-libsecret
Summary:        MinGW Windows GTK+ library
Requires:       pkgconfig

%description -n mingw64-libsecret
GObject based library for accessing the Secret Service API.


%?mingw_debug_package


%prep
%setup -q -n libsecret-%{version}
%patch0 -p1

%build
NOCONFIGURE=1 sh autogen.sh
%mingw_configure

%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

%mingw_find_lang %{name} --all-name

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

%files -n mingw32-libsecret -f mingw32-%{name}.lang
%{mingw32_bindir}/secret-tool.exe
%{mingw32_bindir}/libsecret-1-0.dll
%dir %{mingw32_includedir}/libsecret-1
%dir %{mingw32_includedir}/libsecret-1/libsecret
%{mingw32_includedir}/libsecret-1/libsecret/*
%{mingw32_libdir}/libsecret-1.dll.a
%{mingw32_libdir}/libsecret-1.a
%{mingw32_libdir}/pkgconfig/libsecret-1.pc
%{mingw32_libdir}/pkgconfig/libsecret-unstable.pc
%{mingw32_mandir}/man1/secret-tool.1*

%files -n mingw64-libsecret -f mingw64-%{name}.lang
%{mingw64_bindir}/secret-tool.exe
%{mingw64_bindir}/libsecret-1-0.dll
%dir %{mingw64_includedir}/libsecret-1
%dir %{mingw64_includedir}/libsecret-1/libsecret
%{mingw64_includedir}/libsecret-1/libsecret/*
%{mingw64_libdir}/libsecret-1.dll.a
%{mingw64_libdir}/libsecret-1.a
%{mingw64_libdir}/pkgconfig/libsecret-1.pc
%{mingw64_libdir}/pkgconfig/libsecret-unstable.pc
%{mingw64_mandir}/man1/secret-tool.1*

%changelog
* Fri Feb 16 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.18.5-1
- Initial RPM release
