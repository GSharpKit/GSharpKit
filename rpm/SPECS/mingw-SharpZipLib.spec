%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name SharpZipLib
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib

Name:           mingw-SharpZipLib
Version:        1.0.0
Release:        1%{?dist}
Summary:        SharpZipLib (#ziplib, formerly NZipLib) is a compression library for Zip, GZip, BZip2.

Group:          Development/Languages
License:	MIT
URL:		https://www.nuget.org/packages/SharpZipLib
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:		/usr

BuildArch: 	noarch

Requires:	mono-core >= 5.14.0
BuildRequires:	nuget

%description
SharpZipLib (#ziplib, formerly NZipLib) is a compression library for Zip, GZip, 
BZip2, and Tar written entirely in C# for .NET. It is implemented as an assembly 
(installable in the GAC), and thus can easily be incorporated into other projects 
(in any .NET language)

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-mono

%description -n mingw32-%{mingw_pkg_name}
SharpZipLib (#ziplib, formerly NZipLib) is a compression library for Zip, GZip, BZip2.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-mono

%description -n mingw64-%{mingw_pkg_name}
SharpZipLib (#ziplib, formerly NZipLib) is a compression library for Zip, GZip, BZip2.

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > SharpZipLib32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}/mono

Name: SharpZipLib
Description: %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/SharpZipLib/ICSharpCode.SharpZipLib.dll
Cflags:
EOF

cat > SharpZipLib64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}/mono

Name: SharpZipLib
Description: %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/SharpZipLib/ICSharpCode.SharpZipLib.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/mono/gac
gacutil -i SharpZipLib.%{version}/lib/netstandard2.0/ICSharpCode.SharpZipLib.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 SharpZipLib32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/SharpZipLib.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/mono/gac
gacutil -i SharpZipLib.%{version}/lib/netstandard2.0/ICSharpCode.SharpZipLib.dll -package %{mingw_pkg_name} -root $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir} -gacdir mono/gac

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 SharpZipLib64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/SharpZipLib.pc


%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/mono/gac
%{mingw32_prefix}%{libdir}/mono/SharpZipLib/ICSharpCode.SharpZipLib.dll
%{mingw32_datadir}/pkgconfig/SharpZipLib.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/mono/gac
%{mingw64_prefix}%{libdir}/mono/SharpZipLib/ICSharpCode.SharpZipLib.dll
%{mingw64_datadir}/pkgconfig/SharpZipLib.pc


%changelog
* Wed Nov 13 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 1.0.0-1
- Initial version
