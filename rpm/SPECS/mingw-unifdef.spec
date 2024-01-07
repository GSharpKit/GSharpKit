%?mingw_package_header

%define debug_package %{nil}

%global mingw_build_win32 0
%global mingw_build_win64 1

Summary: Tool for removing ifdef'd lines
Name: mingw-unifdef
Version: 2.10
Release: 17%{?dist}
License: BSD
URL: http://dotat.at/prog/unifdef/
Source0: http://dotat.at/prog/unifdef/unifdef-%{version}.tar.xz
Patch0:	unifdef-2.10-nosnprintf.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: pkgconfig

%description
Unifdef is useful for removing ifdefed lines from a file while otherwise
leaving the file alone. Unifdef acts on #ifdef, #ifndef, #else, and #endif
lines, and it knows only enough about C and C++ to know when one of these
is inactive because it is inside a comment, or a single or double quote.

# Win64
%package -n mingw64-unifdef
Summary: Tool for removing ifdef'd lines

%description -n mingw64-unifdef
Unifdef is useful for removing ifdefed lines from a file while otherwise
leaving the file alone. Unifdef acts on #ifdef, #ifndef, #else, and #endif
lines, and it knows only enough about C and C++ to know when one of these
is inactive because it is inside a comment, or a single or double quote.

%prep
%setup -qn "unifdef-%{version}"
%patch0 -p1

%build
%mingw64_make -f win32/Makefile.mingw

%install
rm -rf $RPM_BUILD_ROOT
install -d -m0755 $RPM_BUILD_ROOT%{mingw64_bindir}
install -p -m0755 unifdef.exe $RPM_BUILD_ROOT%{mingw64_bindir}/unifdef.exe
install -p -m0755 unifdefall.sh $RPM_BUILD_ROOT%{mingw64_bindir}/unifdefall.sh

# Win64
%files -n mingw64-unifdef
%{mingw64_bindir}/unifdef.exe
%{mingw64_bindir}/unifdefall.sh

%changelog
* Mon Oct 24 2022 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 2.10-17
- Initial Mingw build

