%?mingw_package_header

Name:           mingw-libexif
Version:        0.6.21
Release:        1%{?dist}
Summary:        Reads and writes EXIF metainformation from and to image files.

License:        LGPLv2+
Group:          Development/Libraries
URL:            https://libexif.github.io
Source0:        https://sourceforge.net/projects/libexif/files/libexif/%{version}/libexif-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 98
BuildRequires:  mingw64-filesystem >= 98
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2

%description
is a library written in pure portable C.
reads and writes EXIF metainformation from and to image files.
is licensed under the GNU LESSER GENERAL PUBLIC LICENSE Version 2.1 (LGPL).
runs under POSIX systems (e.g. GNU/Linux, xBSD, MacOS X, etc.) and Win32. Win64 untested.


%package -n mingw32-libexif
Summary:        %{summary}

%description -n mingw32-libexif
is a library written in pure portable C.
reads and writes EXIF metainformation from and to image files.
is licensed under the GNU LESSER GENERAL PUBLIC LICENSE Version 2.1 (LGPL).
runs under POSIX systems (e.g. GNU/Linux, xBSD, MacOS X, etc.) and Win32. Win64 untested.

%package -n mingw32-libexif-static
Summary:        %{summary}
Requires:       mingw32-libexif = %{version}-%{release}

%description -n mingw32-libexif-static
is a library written in pure portable C.
reads and writes EXIF metainformation from and to image files.
is licensed under the GNU LESSER GENERAL PUBLIC LICENSE Version 2.1 (LGPL).
runs under POSIX systems (e.g. GNU/Linux, xBSD, MacOS X, etc.) and Win32. Win64 untested.


%package -n mingw64-libexif
Summary:        %{summary}

%description -n mingw64-libexif
is a library written in pure portable C.
reads and writes EXIF metainformation from and to image files.
is licensed under the GNU LESSER GENERAL PUBLIC LICENSE Version 2.1 (LGPL).
runs under POSIX systems (e.g. GNU/Linux, xBSD, MacOS X, etc.) and Win32. Win64 untested.

%package -n mingw64-libexif-static
Summary:        %{summary}
Requires:       mingw64-libexif = %{version}-%{release}

%description -n mingw64-libexif-static
is a library written in pure portable C.
reads and writes EXIF metainformation from and to image files.
is licensed under the GNU LESSER GENERAL PUBLIC LICENSE Version 2.1 (LGPL).
runs under POSIX systems (e.g. GNU/Linux, xBSD, MacOS X, etc.) and Win32. Win64 untested.

%?mingw_debug_package

%prep
%setup -q -n libexif-%{version}

%build
%mingw_configure

%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libexif.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libexif.a

rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}

#sed -i -e 's!/usr/i686-w64-mingw32/sys-root/mingw/lib!/usr/i686-w64-mingw32/sys-root/mingw/bin!g' $RPM_BUILD_ROOT%{mingw32_libdir}/pkgconfig/libexif.pc
#sed -i -e 's!/usr/i686-w64-mingw32/sys-root/mingw/lib!/usr/i686-w64-mingw32/sys-root/mingw/bin!g' $RPM_BUILD_ROOT%{mingw64_libdir}/pkgconfig/libexif.pc

%files -n mingw32-libexif
%{mingw32_bindir}/libexif-12.dll
%dir %{mingw32_includedir}/libexif
%{mingw32_includedir}/libexif/*.h
%{mingw32_libdir}/pkgconfig/libexif.pc

%files -n mingw32-libexif-static
%{mingw32_libdir}/libexif.dll.a

%files -n mingw64-libexif
%{mingw64_bindir}/libexif-12.dll
%dir %{mingw64_includedir}/libexif
%{mingw64_includedir}/libexif/*.h
%{mingw64_libdir}/pkgconfig/libexif.pc

%files -n mingw64-libexif-static
%{mingw64_libdir}/libexif.dll.a

%changelog
* Mon Nov 19 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 0.6.21-1
- Initial RPM release
