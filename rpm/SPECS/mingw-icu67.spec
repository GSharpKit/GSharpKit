%{?mingw_package_header}

%global mingw_build_win32 0
%global mingw_build_win64 1

%global underscore_version %(echo %{version} | sed 's/\\./_/g')
%global dash_version %(echo %{version} | sed 's/\\./-/g')
%global lib_version 67

Name:           mingw-icu67
Version:        67.1
Release:        3%{?dist}
Summary:        MinGW compilation of International Components for Unicode Tools

License:        MIT and UCD and Public Domain
URL:            http://icu-project.org
Source0:        https://github.com/unicode-org/icu/releases/download/release-%{dash_version}/icu4c-%{underscore_version}-src.tgz

# Patch to fix the build from
# https://build.opensuse.org/package/show/windows:mingw:win32/mingw32-icu
Patch0:         icu4c_mingwbuild.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  gcc-c++

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils

%description
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides calendar
support, conversions for many character sets, language sensitive
collation, date and time formatting, support for many locales, message
catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word,
line, and sentence breaking, etc.


# Win64
%package -n mingw64-icu67
Summary:        MinGW compilation of International Components for Unicode Tools

%description -n mingw64-icu67
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides calendar
support, conversions for many character sets, language sensitive
collation, date and time formatting, support for many locales, message
catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word,
line, and sentence breaking, etc.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n icu


%build
pushd source

mkdir -p nativebuild
pushd nativebuild
../configure --enable-static --disable-shared
# Parallel build occasionally broken
%make_build || make
popd

%mingw_configure \
        --enable-shared --disable-static \
        --with-cross-build=$(pwd)/nativebuild \
        --with-data-packaging=library

%mingw_make_build

popd

%install
pushd source
%mingw_make_install
popd

#find %{buildroot} -name "*.dll" -type l -delete

# remove unneded files
rm -fr %{buildroot}%{mingw64_mandir}

rm %{buildroot}%{mingw64_bindir}/icu-config
rm %{buildroot}%{mingw64_libdir}/icu/Makefile.inc
rm %{buildroot}%{mingw64_libdir}/icu/pkgdata.inc

rm %{buildroot}%{mingw64_bindir}/escapesrc.exe
rm %{buildroot}%{mingw64_bindir}/genrb.exe
rm %{buildroot}%{mingw64_bindir}/gencnval.exe
rm %{buildroot}%{mingw64_bindir}/uconv.exe
rm %{buildroot}%{mingw64_bindir}/gencmn.exe
rm %{buildroot}%{mingw64_bindir}/makeconv.exe
rm %{buildroot}%{mingw64_bindir}/genbrk.exe
rm %{buildroot}%{mingw64_bindir}/gensprep.exe
rm %{buildroot}%{mingw64_bindir}/pkgdata.exe
rm %{buildroot}%{mingw64_bindir}/icupkg.exe
rm %{buildroot}%{mingw64_bindir}/derb.exe
rm %{buildroot}%{mingw64_bindir}/genccode.exe
rm %{buildroot}%{mingw64_bindir}/gendict.exe
rm %{buildroot}%{mingw64_bindir}/gencfu.exe
rm %{buildroot}%{mingw64_bindir}/gennorm2.exe
rm %{buildroot}%{mingw64_bindir}/icuinfo.exe

rm %{buildroot}%{mingw64_libdir}/libicudata.dll.a
rm %{buildroot}%{mingw64_libdir}/libicui18n.dll.a
rm %{buildroot}%{mingw64_libdir}/libicuuc.dll.a
rm %{buildroot}%{mingw64_libdir}/libicuio.dll.a
rm %{buildroot}%{mingw64_libdir}/libicutest.dll.a
rm %{buildroot}%{mingw64_libdir}/libicutu.dll.a
rm %{buildroot}%{mingw64_libdir}/pkgconfig/icu-i18n.pc
rm %{buildroot}%{mingw64_libdir}/pkgconfig/icu-io.pc
rm %{buildroot}%{mingw64_libdir}/pkgconfig/icu-uc.pc
rm -rf %{buildroot}%{mingw64_includedir}/unicode
rm -rf %{buildroot}%{mingw64_libdir}/icu
rm -rf %{buildroot}%{mingw64_datadir}/icu


# Win64
%files -n mingw64-icu67

%{mingw64_bindir}/icuio%{lib_version}.dll
%{mingw64_bindir}/icuuc%{lib_version}.dll
%{mingw64_bindir}/icui18n%{lib_version}.dll
%{mingw64_bindir}/icutu%{lib_version}.dll
%{mingw64_bindir}/icudata%{lib_version}.dll
%{mingw64_bindir}/icutest%{lib_version}.dll

%changelog
* Tue Jul 26 2022 Mikkel Kruse Johnsen <mikkel@xmedicus.com>
- Initial release
