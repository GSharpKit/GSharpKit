%{?ucrt_package_header}

%global base libtheora

Name:           ucrt-%{base}
Version:        1.1.1
Release:        28%{?dist}
Summary:        Theora Video Compression Codec

License:        BSD-3-Clause
URL:            http://www.theora.org
Source0:        http://downloads.xiph.org/releases/theora/%{base}-%{version}.tar.xz
# native package and upstream SVN r18268
Patch0:         libtheora-1.1.1-fix-pp_sharp_mod-calc.patch
# native package and upstream SVN r19088
# http://trac.xiph.org/ticket/1947
Patch1:         libtheora-1.1.1-libpng16.patch
# native package and upstream SVN r19087
Patch2:         libtheora-1.1.1-libm.patch
# to fix parallel build with -no-undefined in MinGW
# upstream SVN r16712
Patch3:         libtheora-1.1.1-libadd.patch
# https://trac.xiph.org/ticket/2141
# https://gitlab.xiph.org/xiph/theora/-/issues/2141
Patch4:         mingw-libtheora-1.1.1-rint.patch
Patch5:         mingw-libtheora-getopt.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  autoconf automake libtool
# for autotools
BuildRequires:  SDL-devel

BuildRequires:  ucrt64-filesystem >= 95
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-libogg
BuildRequires:  ucrt64-libvorbis
BuildRequires:  ucrt64-libpng


%description
Theora is Xiph.Org's first publicly released video codec, intended
for use within the Ogg's project's Ogg multimedia streaming system.
Theora is derived directly from On2's VP3 codec; Currently the two are
nearly identical, varying only in encapsulating decoder tables in the
bitstream headers, but Theora will make use of this extra freedom
in the future to improve over what is possible with VP3.


%package -n ucrt64-%{base}
Summary:        %{summary}

%description -n ucrt64-%{base}
Theora is Xiph.Org's first publicly released video codec, intended
for use within the Ogg's project's Ogg multimedia streaming system.
Theora is derived directly from On2's VP3 codec; Currently the two are
nearly identical, varying only in encapsulating decoder tables in the
bitstream headers, but Theora will make use of this extra freedom
in the future to improve over what is possible with VP3.

This package is MinGW compiled theora library for the Win64 target.


%package -n ucrt64-theora-tools
Summary:        Command line tools for Theora videos
Requires:       ucrt64-%{base} = %{version}-%{release}

%description -n ucrt64-theora-tools
The theora-tools package contains simple command line tools for use
with theora bitstreams.

This package is MinGW compiled theora tools for the Win64 target.


%{?ucrt_debug_package}


%prep
%setup -q -n %{base}-%{version}
%patch -P0 -p1
%patch -P1 -p0
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

# no custom CFLAGS please
sed -i 's/CFLAGS="$CFLAGS $cflags_save"/CFLAGS="$cflags_save"/g' configure.ac

# fix syntax of export symbols files
sed -i 's/^EXPORTS//' win32/xmingw32/*.def


%build
autoreconf -fi -I m4
%ucrt64_configure --disable-static

# disable build of documentation
sed -i 's/\<doc\>//' Makefile

%ucrt64_make %{?_smp_mflags}


%install
%ucrt64_make install DESTDIR=%{buildroot} INSTALL="install -p"

mkdir -p %{buildroot}/%{ucrt64_bindir}
pushd examples
../libtool --mode=install install -p -m 755 dump_video.exe %{buildroot}/%{ucrt64_bindir}/theora_dump_video.exe
../libtool --mode=install install -p -m 755 encoder_example.exe %{buildroot}/%{ucrt64_bindir}/theora_encode.exe
../libtool --mode=install install -p -m 755 png2theora.exe %{buildroot}/%{ucrt64_bindir}/png2theora.exe
popd

rm -fv %{buildroot}/%{ucrt64_libdir}/*.la


%files -n ucrt64-%{base}
%doc README COPYING
%{ucrt64_bindir}/libtheora-0.dll
%{ucrt64_bindir}/libtheoradec-1.dll
%{ucrt64_bindir}/libtheoraenc-1.dll
%{ucrt64_includedir}/theora
%{ucrt64_libdir}/libtheora.dll.a
%{ucrt64_libdir}/libtheoradec.dll.a
%{ucrt64_libdir}/libtheoraenc.dll.a
%{ucrt64_libdir}/pkgconfig/theora*.pc

%files -n ucrt64-theora-tools
%{ucrt64_bindir}/*.exe


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Feb 22 2025 František Dvořák <valtri@civ.zcu.cz> - 1.1.1-26
- Fix build on recent MinGW with included getopt
- Update license after migration to SPDX

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.1-24
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.1.1-17
- Rebuild with ucrt-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.1.1-11
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 04 2015 František Dvořák <valtri@civ.zcu.cz> - 1.1.1-2
- Build with the newest toolchain

* Tue Aug 5 2014 František Dvořák <valtri@civ.zcu.cz> - 1.1.1-1
- Initial package
