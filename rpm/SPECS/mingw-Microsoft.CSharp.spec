%?mingw_package_header

%global __strip /bin/true

%global mingw_pkg_name Microsoft.CSharp
%global mingw_build_win32 1
%global mingw_build_win64 1

%define debug_package %{nil}

%define libdir /lib
%define apiversion 4.5.0.0

Name:           mingw-Microsoft.CSharp
Version:        4.5.0
Release:        1%{?dist}
Summary:        Provides support for compilation and code generation, including dynamic, using the C# language.

Group:          Development/Languages
License:        MIT
URL:            https://www.nuget.org/packages/Microsoft.CSharp

Prefix:		/usr
BuildArch:	noarch

BuildRequires:  mono-devel
BuildRequires:  nuget

%description
Provides support for compilation and code generation, including dynamic, using the C# language.

Commonly Used Types:
Microsoft.CSharp.RuntimeBinder.Binder
Microsoft.CSharp.RuntimeBinder.RuntimeBinderException
Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo
Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfoFlags
Microsoft.CSharp.RuntimeBinder.CSharpBinderFlags

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw32-mono

%description -n mingw32-%{mingw_pkg_name}
Provides support for compilation and code generation, including dynamic, using the C# language.

Commonly Used Types:
Microsoft.CSharp.RuntimeBinder.Binder
Microsoft.CSharp.RuntimeBinder.RuntimeBinderException
Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo
Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfoFlags
Microsoft.CSharp.RuntimeBinder.CSharpBinderFlags

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:       %{summary}
Requires:       mingw64-mono

%description -n mingw64-%{mingw_pkg_name}
Provides support for compilation and code generation, including dynamic, using the C# language.

Commonly Used Types:
Microsoft.CSharp.RuntimeBinder.Binder
Microsoft.CSharp.RuntimeBinder.RuntimeBinderException
Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfo
Microsoft.CSharp.RuntimeBinder.CSharpArgumentInfoFlags
Microsoft.CSharp.RuntimeBinder.CSharpBinderFlags

%prep
%setup -c %{name}-%{version} -T
nuget install %{mingw_pkg_name} -Version %{version}

cat > Microsoft.CSharp32.pc << \EOF
prefix=%{mingw32_prefix}
exec_prefix=${prefix}
libdir=%{mingw32_prefix}%{libdir}

Name: Microsoft.CSharp
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/Microsoft.CSharp.dll
Cflags:
EOF

cat > Microsoft.CSharp64.pc << \EOF
prefix=%{mingw64_prefix}
exec_prefix=${prefix}
libdir=%{mingw64_prefix}%{libdir}

Name: Microsoft.CSharp
Description: %{name} - %{summary}
Requires:
Version: %{version}
Libs: -r:${libdir}/Microsoft.CSharp.dll
Cflags:
EOF


%build

%install
%{__rm} -rf %{buildroot}

# Mingw32
install -d -m 755 $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}
install -m 644 Microsoft.CSharp.%{version}/lib/netstandard2.0/Microsoft.CSharp.dll $RPM_BUILD_ROOT%{mingw32_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/
install -m 644 Microsoft.CSharp32.pc $RPM_BUILD_ROOT%{mingw32_datadir}/pkgconfig/Microsoft.CSharp.pc

# Mingw64
install -d -m 755 $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}
install -m 644 Microsoft.CSharp.%{version}/lib/netstandard2.0/Microsoft.CSharp.dll $RPM_BUILD_ROOT%{mingw64_prefix}%{libdir}/

install -d -m 755 $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/
install -m 644 Microsoft.CSharp64.pc $RPM_BUILD_ROOT%{mingw64_datadir}/pkgconfig/Microsoft.CSharp.pc

%clean
#%{__rm} -rf %{buildroot}

%files -n mingw32-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw32_prefix}%{libdir}/Microsoft.CSharp.dll
%{mingw32_datadir}/pkgconfig/Microsoft.CSharp.pc

%files -n mingw64-%{mingw_pkg_name}
%defattr(-,root,root,-)
%{mingw64_prefix}%{libdir}/Microsoft.CSharp.dll
%{mingw64_datadir}/pkgconfig/Microsoft.CSharp.pc

%changelog
* Mon Nov 12 2018 Mikkel Kruse Johnsen <mikkel@xmedicus.com> - 4.5.0-1
- Initial version
